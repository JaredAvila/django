from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):

    return render(request, 'courses/index.html', {"courses": Course.objects.all()})

def confirm(request):
    return render(request, 'courses/confirm.html')

def delete(request):
    print('Am i here?')
    print(request.POST)
    x = Course.objects.get(id=request.POST['id'])
    x.delete()

    return redirect('/courses')

def processing(request):
    errors = Course.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/courses')
    new = Course(name=request.POST['name'], desc = request.POST['desc'])
    new.save()
    return redirect('/courses')
