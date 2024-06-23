from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import authenticate, login, logout

from .common import *
from .models import User

# Create your views here.
def index(request):
    is_sign_in = False
    context = {

    }
    return render(request, 'sport/index.html', context)


def sign_up(request):
    return render(request, 'sport/sign_up.html')


def sign_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Sign in successful!')
            return redirect('sport:index')
        else:
            messages.error(request, 'Invalid email or password')
            print('error')
        return redirect('sign_in')
    else:
        return render(request, 'sport/sign_in.html')
    

def sign_out(request):
    pass


def add_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        created_date = datetime.now()
        user = User.objects.create(
            email=email,
            username=username,
            password=password,
            created_date=created_date,
        )
        user.save()
        return HttpResponse('success')
    else:
        return HttpResponse('Invalid request method', status=405)





