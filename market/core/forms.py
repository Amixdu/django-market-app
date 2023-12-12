from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter username',
        'class': 'mt-1 p-2 w-full border rounded-md'
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter email',
        'class': 'mt-1 p-2 w-full border rounded-md'
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter password',
        'class': 'mt-1 p-2 w-full border rounded-md',
        'type': 'password'
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter password',
        'class': 'mt-1 p-2 w-full border rounded-md',
        'type': 'password'
    }))

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter username',
        'class': 'mt-1 p-2 w-full border rounded-md'
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter password',
        'class': 'mt-1 p-2 w-full border rounded-md',
        'type': 'password'
    }))
