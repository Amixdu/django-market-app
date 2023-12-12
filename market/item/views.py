from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Item, Category
from . import forms


@login_required
def items(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    query = request.GET.get('q', '')
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    category_id = request.GET.get('category', 0)
    if category_id:
        items = items.filter(category__id=category_id)

    return render(
        request,
        "item/items.html",
        {
            "items": items,
            "categories": categories,
            "q": query,
            "category_id": int(category_id)
        },
    )


@login_required
def item(request, id):
    item = get_object_or_404(Item, pk=id)
    related_items = Item.objects.filter(
        created_by=item.created_by, is_sold=False
    ).exclude(pk=id)[0:5]
    return render(
        request, "item/item.html", {"item": item, "related_items": related_items}
    )


@login_required
def create(request):
    if request.method == "POST":
        form = forms.NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect("item:item", id=item.id)
    else:
        form = forms.NewItemForm()
    return render(request, "item/form.html", {"form": form, "title": "Add item"})


@login_required
def delete(request, id):
    item = get_object_or_404(Item, pk=id, created_by=request.user)
    item.delete()

    return redirect("dashboard:index")


@login_required
def update(request, id):
    item = get_object_or_404(Item, pk=id, created_by=request.user)

    if request.method == "POST":
        form = forms.UpdateItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()

            return redirect("item:item", id=item.id)
    else:
        form = forms.UpdateItemForm(instance=item)
    return render(request, "item/form.html", {"form": form, "title": "Edit item"})
