from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    request.session['ran_str'] = get_random_string(length = 14)
    request.session['generate'] = request.POST
    
    try:
        request.session['counter']
    except KeyError:
        request.session['counter'] = 0
    
    request.session['counter']+= 1
    return render(request, "rand/index.html")

def reset(request):
    del request.session['counter']
    return redirect('/')

# Create your views here.
