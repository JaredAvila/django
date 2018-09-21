from django.shortcuts import render, redirect, HttpResponse
from apps.ajax_demo.models import *
from django.contrib import messages
from django.core import serializers
import json

def index(request):
    return render(request, 'ajax_demo/index.html')

def allJSON(request):
    users = User.objects.all()
    usersJson = serializers.serialize('json', users)
    return HttpResponse(usersJson, content_type='application/json')

def allHTML(request):
    users = User.objects.all()
    return render(request, 'ajax_demo/all.html', {"users": users})

def find(request):
    users = User.objects.filter(fName__startswith = request.POST['fNameStartsWith'])
    return render(request, 'ajax_demo/all.html', {"users": users})

def create(request):
    print("in create")
    new = User(fName = request.POST['fName'], lName = request.POST['lName'], email = request.POST['email'])
    new.save()
    users = User.objects.all().order_by('-id')
    print(users)
    return render(request, 'ajax_demo/all.html', {"users": users})
