# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput



class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(widget=PasswordInput, label='Hasło')
        
        
    