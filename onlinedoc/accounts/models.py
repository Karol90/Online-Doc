# coding=utf-8

from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    # Old way
    # user = models.ForeignKey(User, unique=True)
    
    # New way
    user = models.OneToOneField(User)
    
    # Fields
    firstname = models.CharField(max_length=20, verbose_name='Imię')
    lastname = models.CharField(max_length=20, verbose_name='Nazwisko')
    address = models.TextField(max_length=100, verbose_name='Adres')
    city = models.CharField(max_length=20, verbose_name='Miejscowość')
    postalcode = models.CharField(max_length=10, verbose_name='Kod pocztowy')
    country = models.CharField(max_length=20, null=True, blank=True, verbose_name='Kraj')
    pesel = models.CharField(max_length=11, verbose_name='PESEL')
    nip = models.CharField(max_length=10, verbose_name='NIP')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Data urodzenia')
    activation_key = models.CharField(max_length=40, null=True, blank=True)
    key_expires = models.DateTimeField(null=True, blank=True)
    
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
    title = models.CharField(max_length=10, null=True, blank=True, verbose_name='Tytuł')
    bio = models.TextField(null=True, blank=True, verbose_name='Biografia??')
    
    class Meta: 
        verbose_name = "Lekarz"
        verbose_name_plural = "Lekarze"