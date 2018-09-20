from django.shortcuts import render, redirect, HttpResponse
import bcrypt
import datetime
from apps.amadon.models import *

def index(request):
    request.session['userId'] = 1
    request.session['peaceId'] = Item.objects.get(id=1).vId
    request.session['showId'] = Item.objects.get(id=2).vId
    request.session['scaryId'] = Item.objects.get(id=3).vId
    request.session['mathId'] = Item.objects.get(id=4).vId
    request.session['appleId'] = Item.objects.get(id=5).vId
    request.session['peaceName'] = Item.objects.get(id=1).name
    request.session['showName'] = Item.objects.get(id=2).name
    request.session['scaryName'] = Item.objects.get(id=3).name
    request.session['mathName'] = Item.objects.get(id=4).name
    request.session['appleName'] = Item.objects.get(id=5).name
    request.session['peaceDesc'] = Item.objects.get(id=1).desc
    request.session['showDesc'] = Item.objects.get(id=2).desc
    request.session['scaryDesc'] = Item.objects.get(id=3).desc
    request.session['mathDesc'] = Item.objects.get(id=4).desc
    request.session['appleDesc'] = Item.objects.get(id=5).desc
    request.session['peacePrice'] = Item.objects.get(id=1).price
    request.session['showPrice'] = Item.objects.get(id=2).price
    request.session['scaryPrice'] = Item.objects.get(id=3).price
    request.session['mathPrice'] = Item.objects.get(id=4).price
    request.session['applePrice'] = Item.objects.get(id=5).price
    return render(request, 'amadon/index.html')

def confirm(request):
    print('you have not been double charged. have a nice day =)')
    return render(request,'amadon/confrimation.html')

def checkout(request):
    print('you have been charged! Enjoy your t-shirt')
    price = Item.objects.get(vId=request.POST['vId']).price
    request.session['orderTotal'] = int(price) * int(request.POST['qty'])
    item = Item.objects.get(vId=request.POST['vId'])
    user = User.objects.get(id = request.session['userId'])
    
    for i in range(int(request.POST['qty'])):
        new = Purchase(userId = user, itemId = item)
        new.save()
    totesMagotes = Purchase.objects.all().filter(userId = request.session['userId']).values()
    totalItems = 0
    totalSpent = 0
    for item in totesMagotes:
        totalItems += 1
        totalSpent += Item.objects.get(id = item['itemId_id']).price
    request.session['totalItems'] = totalItems
    request.session['totalSpent'] = totalSpent
    return redirect('/confirm')