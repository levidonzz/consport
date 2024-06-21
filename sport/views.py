from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .common import *
from .form import UserForm

# Create your views here.
def index(request):
    user_list = get_user_list()
    context = {
        'user_list': user_list
    }
    return render(request, 'sport/index.html', context)


def sign_up(request):
    context = {
        'userForm': UserForm
    }
    return render(request, 'sport/sign_up.html', context)


def sign_in(request):
    return HttpResponse('success')


def add_user(request):
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    created_date = datetime.now()
    user = User.objects.create(email=email, username=username, password=password, liked_sport=None, created_date=created_date)
    user.save()
    return HttpResponse('success')





