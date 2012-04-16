# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from django.forms.models import ModelForm

from onlinedoc.accounts.models import Account


class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(widget=PasswordInput, label='Hasło')
        
class RegisterForm(ModelForm):
    class Meta:
        model = Account
        exclude = ('user',)