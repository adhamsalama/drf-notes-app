from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import User

# Create your models here.

class Note(models.Model):
    content = models.TextField(blank=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
