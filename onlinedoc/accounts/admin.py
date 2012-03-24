from django.contrib import admin
from accounts.models import Account, Doctor, Patient

admin.site.register(Account)
admin.site.register(Patient)
admin.site.register(Doctor)