from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def recipeValidator(self, postData):
        errors={}

        if postData['recipeName'] =='' or postData['desc'] == '' or postData['inst'] == '':
            errors['recipe'] = 'Cannot leave fields blank'
            return errors
        return errors

    def loginValidator(self, postData):
        errors ={}
        emailRegEx = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        try:
            if len(postData['userName']) == 0 or len(postData['password']) == 0:
                errors['blank'] = "Must fill out all fields"
                return errors
            if len(postData['email']) == 0  or len(postData['fName']) == 0  or len(postData['lName']) == 0:
                errors['blank'] = "Must fill out all fields"
                return errors
            if len(postData['userName']) < 4:
                errors['userName'] = "Username is too short"
            if postData['password'] != postData['confPassword']:
                errors['password'] = 'Passwords do not match'
                return errors
            if bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', postData['password'])) == False:
                errors['password'] = 'Password must contain a number and a letter'
                return errors
            if len(postData['password']) < 7:
                errors['password'] = 'Password must be at least 8 characters'
                return errors
            if not emailRegEx.match(postData['email']):
                errors['email'] = 'Invalid email'
                return errors
            #replace next line with database query to check if user name is in db and/or email, need two checks, one for each. sepparate messages.
            if postData == True:
                errors['database'] = 'Username or email already exists'
                return errors
        except:
            print("except: checking database")
            #replace next line with database query to check if user name is in db and/or password matches
            if postData['userName'] == "happy":
                errors['userName'] = 'Username or password incorrect'
                return errors
        return errors
    def loggedIn(self, postData):
        validHash = User.objects.get(userName = postData['userName']).hashId
        if validHash != postData['hashId']:
            return False
        else:
            return True
        

        

class User(models.Model):
    userName = models.CharField(max_length=255)
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hashId = models.CharField(max_length=255, default='abracadabraB')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(1000, default="I'm hungry")
    ingr = models.TextField(1000, default="I'm hungry")
    inst = models.TextField(1000, default="I'm hungry")
    userId = models.ForeignKey(User, related_name='userRecipes', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Comment(models.Model):
    comment = models.TextField(1000, default='Comment')
    user_id = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, related_name="recipes", on_delete = models.CASCADE, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Likes(models.Model):
    objects = UserManager()


