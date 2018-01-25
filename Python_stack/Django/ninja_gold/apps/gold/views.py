from django.shortcuts import render, HttpResponse, redirect
import random
import time
import datetime

now = datetime.datetime.now().strftime("%y/%m/%d %H:%M")

def index(request):
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0
    try:
        request.session['message']
    except KeyError:
        request.session['message'] = []
    return render(request, "gold/index.html")

def process(request, location):
    if request.method == 'POST':
        if location == "farm":
            gold = random.randint(10,20)
            message = "Earned " + str(gold) + " golds from the " + location + " " + (now)
        if location == "cave":
            gold = random.randint(5,10)
            message = "Earned " + str(gold) + " golds from the " + location + " " + (now)
        if location == "house":
            gold = random.randint(2,5)
            message = "Earned " + str(gold) + " golds from the " + location + " " + (now)
        if location == "casino":
            gold = random.randint(-50,50)
            if gold > 0:
                message = "Earned " + str(gold) + " golds from the " + location  + " " +(now) 
            else:
                message = "Entered the " + location + " and lost " + str(-gold) + " golds...Ouch..." + " " + (now)    
    
    request.session['gold'] += gold
    request.session['message'].append(message)
            
    return redirect('/')
def reset(request):
    del request.session['gold']
    del request.session['message']
    return redirect('/')

