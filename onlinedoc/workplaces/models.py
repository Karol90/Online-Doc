from django.db import models
from accounts.models import Doctor
    
class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=20)
    postalcode = models.CharField(max_length=10)
    country = models.CharField(max_length=20, null=True, blank=True)
    
class Place(models.Model):
    name = models.CharField(max_length=10)
    location = models.ForeignKey(Location)
    doctor = models.ManyToManyField(Doctor)