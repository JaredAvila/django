from django.shortcuts import render, redirect, HttpResponse
from .models import User



def index(request):
    context ={
        "users" : User.objects.values()
    }
    response = 'hello there!'
    return HttpResponse(context['users'][2]['first_name'])
