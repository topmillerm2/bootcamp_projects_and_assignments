from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*"*50
    return redirect("/")
def show(request, number):
    response = "placeholder to display blog {}".format(number)
    return HttpResponse(response)
def edit(request, number):
    response = "placeholder to edit blog {}".format(number)
    return HttpResponse(response)
def destroy(request, number):
    return redirect('/')


# Create your views here.
