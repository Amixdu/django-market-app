from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from item.models import Category, Item

from .forms import SingupForm



@login_required
def index(request):
    items = Item.objects.filter(is_sold=False)[0:4]
    categories = Category.objects.all()
    return render(
        request, "core/index.html", {"categories": categories, "items": items}
    )

@login_required
def contact(request):
    return render(request, "core/contact.html")


def signup(request):
    if request.method == "POST":
        form = SingupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/login/")

    else:
        form = SingupForm()

    return render(request, "core/signup.html", {"form": form})
