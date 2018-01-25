from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages


def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'users/index.html', context)

def display(request, number):
    info = User.objects.filter(id=number)
    context = {
        "users": info,
    }
    return render(request, 'users/display.html', context)

def new(request):
    return render(request, 'users/new_user.html')

def create(request):
    if request.method == "POST":
        if len(request.POST['full_name']) == 0 or len(request.POST['email']) == 0:
            messages.error(request, 'All fields must be filled out!')
            return redirect ('/users/new')
        if not request.POST['full_name'].isalpha():
            messages.error(request, 'Name can only contain letters!')
            return redirect ('/users/new')

        user = User.objects.create(full_name = request.POST['full_name'], email = request.POST['email']) 
        user_id = user.id
        context = {
            "users": user,
        }
        return redirect('/users/{}'.format(user_id), context)

def delete(request, number):
    user = User.objects.filter(id = number).delete()

    return redirect('/users')

def update(request, number):
    if request.method == "POST":
        if len(request.POST['full_name']) == 0 or len(request.POST['email']) == 0:
            messages.error(request, 'All fields must be filled out!')
            return redirect ('users/{}/edit'.format(number))
        if not request.POST['full_name'].isalpha():
            messages.error(request, 'Name can only contain letters!')
            return redirect ('users/{}/edit'.format(number))
        user = User.objects.filter(id = number).update(full_name = request.POST['full_name'], email = request.POST['email'])

        return redirect('users/{}'.format(number))

def edit(request, number):
    info = User.objects.filter(id=number)
    context = {
        "users": info,
    }
    return render(request, 'users/edit.html', context)
