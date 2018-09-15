from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.utils.crypto import get_random_string

def index(request):
    print("i am in index")
    if request.session.get('count'):
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    content = {
        "string" : get_random_string(14),
        "count" : request.session['count']
    }
    return render(request, "random_word/index.html", content)

def gen(request):
    return redirect('/random_word')

def reset(request):
    print("i am in reset")
    request.session['count'] = 0
    return redirect('/random_word', request)

# Create your views here.
