from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class Note(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    date = models.DateTimeField(auto_now_add=True)
    