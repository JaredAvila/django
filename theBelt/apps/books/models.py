from __future__ import unicode_literals
from django.db import models
from apps.login.models import User
import bcrypt

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BookReview(models.Model):
    review = models.TextField(max_length=1000, default=None)
    rating = models.IntegerField()
    user_id = models.ForeignKey(User, related_name='userReviews', on_delete=models.CASCADE, default=None)
    book_id = models.ForeignKey(Book, related_name='bookReviews', on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)