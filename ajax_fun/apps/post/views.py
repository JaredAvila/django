from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.core import serializers
import json

def index(request):
    return render(request, 'post/index.html', {"notes": Note.objects.all()})

def validate(request):
    new = Note(note= request.POST['note'])
    new.save()
    return render(request, 'post/post.html', {"notes": Note.objects.all()})
