from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Hero
# Create your views here.

def form(request):
    return render(request, 'form.html')

def registeration(request):
    fname =  request.POST['fname']
    lname =  request.POST['lname']
    email =  request.POST['email']
    password =  request.POST['pass']
    password1 = request.POST['pass1']
    username = request.POST['hero']

    if password == password1:
        if User.objects.filter(username = username).exists():
            messages.info(request, 'Hero name already taken')
            return redirect('form')
        elif User.objects.filter(email = email).exists():
            messages.info(request, 'Email already registered')
            return redirect('form')
        else:
             user = User.objects.create_user(username = username, password = password, email = email, first_name = fname, last_name = lname)
             #user.save();
             #hero = Hero.objects.all()
             return render(request, 'login1.html')
    else :
        messages.info(request, 'Password not matching')
        return redirect('form')
    
def login1(request):
    return render(request, 'login1.html')

def marvel(request):
    username =  request.POST['hero']
    password =  request.POST['pass']

    user = auth.authenticate(username = username, password = password)
    if user is not None:
        auth.login(request, user)
        hero = Hero.objects.all()
        return render(request, 'marvel.html', {'hero':hero})
    else:
        messages.error(request,'Invalid credentials')
        return redirect('login1')

def logout(request):
    auth.logout(request)
    return redirect('form')

    