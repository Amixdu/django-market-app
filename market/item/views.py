from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import NewItemForm


@login_required
def detail(request, id):
    item = get_object_or_404(Item, pk=id)
    related_items = Item.objects.filter(
        created_by=item.created_by, is_sold=False
    ).exclude(pk=id)[0:5]
    return render(
        request, "item/detail.html", {"item": item, "related_items": related_items}
    )


@login_required
def create(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect("item:detail", id=item.id)
    else:
        form = NewItemForm()
    return render(request, "item/form.html", {"form": form})
