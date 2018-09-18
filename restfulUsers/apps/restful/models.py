from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.TimeField(auto_now=True)
