from __future__ import unicode_literals
from django.db import models

class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) == '' or len(postData['last_name']) == '':
            errors['name'] = "Name cannot be left blank"
        return errors

class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    objects = userManager()

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField(default='description')
    uploader = models.ForeignKey(User, related_name='uploaded_books', on_delete=models.CASCADE, null=True)
    liked_users = models.ManyToManyField(User, related_name='liked_books')
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.TextField(default='notes')
    books = models.ManyToManyField(Book, related_name='authors')
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)