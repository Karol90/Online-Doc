# coding=utf-8
from django.db import models
from accounts.models import Doctor

class Worktime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    
    DAY_CHOICES = (
                    (MONDAY,    'Poniedziałek'), 
                    (TUESDAY,   'Wtorek'),
                    (WEDNESDAY, 'Środa'),
                    (THURSDAY,  'Czwartek'),
                    (FRIDAY,    'Piątek'),
                    (SATURDAY,  'Sobota'),
                    (SUNDAY,    'Niedziela'),
                   )
    day = models.IntegerField(choices=DAY_CHOICES, default=MONDAY)
    
    doctor_id = models.ForeignKey(Doctor)
    
class WorktimeExclusions(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    doctor = models.ForeignKey(Doctor)

