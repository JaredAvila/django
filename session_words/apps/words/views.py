from django.shortcuts import render, redirect, HttpResponse
import time


def index(request):
    return render(request, "words/index.html")


def word(request):
    temp = request.session['words']
    temp.append(request.POST)
    request.session['words'] = temp
    return redirect('/')

def clear(request):
    request.session['words'] = []
    return redirect('/')