# Imports.
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Models.
from .models import CustomUser


# Custom forms go here.
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
