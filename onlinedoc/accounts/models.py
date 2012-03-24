from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=20)
    postalcode = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    pesel = models.CharField(max_length=11)
    nip = models.CharField(max_length=10)
    birth_date = models.DateField()
    user = models.ForeignKey(User, unique=True)
    
    def to_string(self):
        return '' + self.firstname + ' ' + self.lastname + ' ' + self.address + ' ' + self.city + ' ' + self.postalcode + ' ' + self.country

    class Admin:
        pass