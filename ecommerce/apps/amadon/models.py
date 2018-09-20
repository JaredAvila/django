from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Item(models.Model):
    name = models.CharField(max_length=255)
    vId = models.CharField(max_length=255)
    price = models.IntegerField(default=None)
    desc = models.TextField(1000, default="No description provided.")

class Purchase(models.Model):
    userId = models.ForeignKey(User, related_name='user_purchases', on_delete=models.CASCADE, null=True)
    itemId = models.ForeignKey(Item, related_name='purchased_item', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)