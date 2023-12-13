from django import forms

from . import models


class NewConversationMessageForm(forms.ModelForm):
    class Meta:
        model = models.ConversationMessage
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "w-full mb-2 p-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 h-40"
                }
            )
        }


class UpdateConversationMessageForm(forms.ModelForm):
    class Meta:
        model = models.ConversationMessage
        fields = ("content",)
        widgets = {
            "content": forms.TextInput(
                attrs={
                    "class": "flex-1 border rounded-full p-2 focus:outline-none focus:border-blue-500"
                }
            ),
            "placeholder": "Type your message...",
        }
