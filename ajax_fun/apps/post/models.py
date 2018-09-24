
from __future__ import unicode_literals
from django.db import models

class Note(models.Model):
    note = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)