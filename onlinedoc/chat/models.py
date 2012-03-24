from django.db import models

# Create your models here.
class Chat(models.Model):
    ON_STATUS           = 1
    INVISIBLE_STATUS    = 2
    OFF_STATUS          = 3
    
    STATUS_CHOICES = (
                        (ON_STATUS, 'On'), 
                        (INVISIBLE_STATUS, 'Invisible'),
                        (OFF_STATUS, 'Off'),
                      )
    
    status = models.IntegerField(choices=STATUS_CHOICES, default=ON_STATUS)
    
    # Active this module in django admin
    class Admin:
        pass
    
    class Meta: 
        verbose_name = "Chat"
        verbose_name_plural = "Chaty"