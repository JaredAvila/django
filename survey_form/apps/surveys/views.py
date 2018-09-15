from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import time
from django.utils.crypto import get_random_string

def index(request):
    return render(request, "surveys/index.html")

def process(request):
    print(request.POST['name'])
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/success')

def success(request):
    return render(request, "surveys/success.html")