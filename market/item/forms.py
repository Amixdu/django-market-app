from django import forms

from .models import Item


INPUT_CLASSES = "w-full mb-2 p-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "price", "category", "image")

        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": f"{INPUT_CLASSES} h-40"}),
            "price": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "category": forms.Select(attrs={"class": INPUT_CLASSES}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }
