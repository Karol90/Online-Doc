from administration.models import UserProfile
from django.contrib.auth.models import User

from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Imie', {'fields': ['firstname']}), 
        ('Nazwisko', {'fields': ['lastname']}),
    ]

admin.site.register(UserProfile, UserProfileAdmin)
