from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

def index(request):
    return render(request, 'django_gold/index.html')

def process(request):
    print(request.POST['postType'])
    x = datetime.datetime.now().strftime("%a, %B %d, %Y")
    request.session['color'] = "green"
    try:
        activity = request.session['activity']
        gold = request.session['gold']
    except:
        activity = []
        gold = 0
    if request.POST['postType'] == 'farm':
        money = random.randrange(10, 21)
        gold += money
        activ = "<p style='color: green;'>You visited a farm on " + str(x) + " and earned:" + str(money) + '</p>'
    if request.POST['postType'] == 'cave':
        money = random.randrange(5, 11)
        gold += money
        activ = "<p style='color: green;'>You visited a cave on " + str(x) + " and earned:" + str(money) + '</p>'
    if request.POST['postType'] == 'house':
        money = random.randrange(2, 5)
        gold += money
        activ = "<p style='color: green;'>You visited a house on " + str(x) + " and earned:" + str(money) + '</p>'
    if request.POST['postType'] == 'Gold Saucer':
        money = random.randrange(-50, 51)
        gold += money
        if money > 0:
            activ = "<p style='color: green;'>You visited The Gold Saucer on " + str(x) + " and earned:" + str(money) + '</p>'
        else:
            activ = "<p style='color: red;'>You visited The Gold Saucer on " + str(x) + " and lost:" + str(money) + '</p>'
            request.session['color'] = 'red'
    request.session['gold'] = gold 
    activity.append(activ)
    request.session['activity'] = activity
    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['activity'] = []
    return redirect('/')