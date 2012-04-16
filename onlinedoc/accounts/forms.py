# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from django.forms.models import ModelForm

from onlinedoc.accounts.models import Account
from django.core.validators import RegexValidator


class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(widget=PasswordInput, label='Hasło')
        
class RegisterForm(ModelForm):
    username = forms.CharField(label="Nazwa użytkownika")
    password = forms.CharField(widget=PasswordInput, label='Hasło')
    confirm_password = forms.CharField(widget=PasswordInput, label='Potwierdź hasło')
    email = forms.EmailField(label='Email')
    
    class Meta:
        model = Account
        fields = ('username', 'password', 'confirm_password', 'email', 'firstname', 'lastname', 'address', 'city',
                  'postalcode', 'country', 'pesel', 'nip', 'birth_date',)
        
    def clean_password(self):
        if self.data['password'] != self.data['confirm_password']:
            raise forms.ValidationError('Hasła nie są identyczne')
        return self.data['password']
    
    def clean_postalcode(self):
        import re
        if re.match(r'[0-9]{2}-[0-9]{3}',  self.data['postalcode']) == None:
            raise forms.ValidationError('Niepoprawny format. (00-000)')
        return self.data['postalcode']
    
    def clean_pesel(self):
        if self.data['pesel'].isdigit()==False or len(self.data['pesel'])<11:
            raise forms.ValidationError('Niepoprawny numer PESEL')
        return self.data['pesel']
    
    def clean_nip(self):
        if self.data['nip'].isdigit()==False or len(self.data['nip'])<10:
            raise forms.ValidationError('Niepoprawny numer NIP')
        return self.data['nip']