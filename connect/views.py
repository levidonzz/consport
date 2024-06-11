from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import User, Sport, Contest


# Create your views here.
def index(request):
    user_list = User.objects.all()
    print(user_list)
    template = loader.get_template('connect/users.html')
    context = {
        'user_list': user_list
    }
    return HttpResponse(template.render(context, request))


def all_contest(request):
    contest_list = Contest.objects.all()
    output = ','.join([contest.name for contest in contest_list])
    return HttpResponse(output)


def all_user(request):
    user_list = User.objects.all()
    output = ','.join([user for user in user_list])
    return HttpResponse(output)