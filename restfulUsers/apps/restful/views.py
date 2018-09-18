from django.shortcuts import render, HttpResponse, redirect
import datetime
from .models import *

def index(request):
    return render(request, 'restful/index.html', {'users': User.objects.all()})

def edit(request):
    return render(request, 'restful/edit.html')

def processing(request):
    if request.POST['action'] == 'Delete':
        print('delete')
        return redirect('/delete')
    print('edit')
    return redirect('/edit')

def delete(request):
    return render(request, 'restful/delete.html')

def add(request):
    return render(request, 'restful/add.html')

def addUser(request):
    fName = request.POST['firstName']
    lName = request.POST['lastName']
    uEmail = request.POST['email']
    user = User(firstName = fName, lastName = lName, email = uEmail)
    user.save()
    return redirect('/')