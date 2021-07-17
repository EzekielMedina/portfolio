from django.db import models
from datetime import datetime


class Message(models.Model):
    usermessage = models.CharField(max_length=55)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now=True, null=True, blank=True)

# Create your models here.
