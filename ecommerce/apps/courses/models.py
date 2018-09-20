from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validator(self, postData):
        errors={}

        if postData['name'] =='' or postData['desc'] == '':
            errors['course'] = 'Cannot leave fields blank'
            return errors
        if len(postData['desc']) < 6:
            errors['course'] = 'description is too short'
        return errors


class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(1000, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
