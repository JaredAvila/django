from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# from models import *

def index(request):

    return render(request, "blogs/index.html")

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['email'] = request.POST['email']
        return redirect('/')
    else:
        return redirect('/')
def show(request, number):
    response = "placeholder to display blog "
    return HttpResponse(response + number)

def edit(request, number):
    edit = "placeholder to edit blog "
    return HttpResponse(edit + number)

def destroy(request, number):
    print("destroyed")
    return redirect('/')