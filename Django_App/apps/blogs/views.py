from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
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