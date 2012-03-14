# -*- coding: utf-8 -*-
from administration.models import UserProfile
from django.contrib.auth.models import User

from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Imie',            {'fields': ['firstname']}), 
        ('Nazwisko',        {'fields': ['lastname']}),
        ('Adres',           {'fields': ['address']}),
        ('Miasto',          {'fields': ['city']}),
        ('Kod pocztowy',    {'fields': ['postalcode']}),
        ('Kraj',            {'fields': ['country']}),
        ('PESEL',           {'fields': ['pesel']}),
        ('NIP',             {'fields': ['nip']}),
        ('Data urodzenia',  {'fields': ['birth_date']}),
        ('Uzytkownik',      {'fields': ['user']})
    ]

admin.site.register(UserProfile, UserProfileAdmin)
