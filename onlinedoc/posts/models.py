from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    status = models.CharField(max_length=10)
    date = models.DateTimeField()
    modified = models.DateTimeField()
    author = models.OneToOneField(User)
