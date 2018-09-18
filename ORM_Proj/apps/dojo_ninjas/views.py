from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response = "Yo!"
    return HttpResponse(response)
