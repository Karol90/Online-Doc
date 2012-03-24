# coding=utf-8

from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    # Old way
    # user = models.ForeignKey(User, unique=True)
    
    # New way
    user = models.OneToOneField(User)
    
    # Fields
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=20)
    postalcode = models.CharField(max_length=10)
    country = models.CharField(max_length=20, null=True, blank=True)
    pesel = models.CharField(max_length=11)
    nip = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)
    
    # __unicode__ is toString() in Java
    def __unicode__(self):
        return self.user.username
    
    class Meta: 
        verbose_name = "Konto"
        verbose_name_plural = "Konta"
        
class Patient(Account):
    account = models.OneToOneField(Account)
    
    class Meta: 
        verbose_name = "Pacjent"
        verbose_name_plural = "Pacjenci"
        
class Doctor(Account):
    account = models.OneToOneField(Account)
    title = models.CharField(max_length=10, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    class Meta: 
        verbose_name = "Lekarz"
        verbose_name_plural = "Lekarze"