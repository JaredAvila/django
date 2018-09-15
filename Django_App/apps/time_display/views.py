from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import time
from django.utils.crypto import get_random_string

# from models import *

def index(request):
    content = {
        "time" : time.asctime( time.localtime(time.time()) )
    }
    return render(request, "time_display/index.html", content)