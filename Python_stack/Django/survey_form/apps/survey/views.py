from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

    try:
        request.session['counter']
    except KeyError:
        request.session['counter'] = 0
    
    request.session['counter']+= 1
    return redirect('survey/result')
def result(request):
    return render(request, 'survey/result.html')
def reset(request):
    return redirect('/')
    

# Create your views here.
