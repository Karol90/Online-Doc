# coding=utf-8
from django.db import models
from accounts.models import Doctor, Patient

class VisitCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Visit(models.Model):
    description = models.TextField(max_length=255)
    visit_time = models.DateTimeField()
    added_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    
    BEFORE_STATUS = 1
    AFTER_STATUS = 2
    CANCELED_STATUS = 3
    
    STATUS_CHOICES = (
                    (BEFORE_STATUS,     'Przed wizytą'), 
                    (AFTER_STATUS,      'Po wizycie'),
                    (CANCELED_STATUS,   'Odwołano'),
                   )
    status = models.IntegerField(choices=STATUS_CHOICES, default=BEFORE_STATUS)
    
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    visit_category = models.ForeignKey(VisitCategory)
    
    
