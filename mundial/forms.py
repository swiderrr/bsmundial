from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from mundial.models import Account

class AccountAuthenticationForm(forms.Form):
    username = forms.CharField(label = "username")
    password = forms.CharField(label= "password", widget=forms.PasswordInput)