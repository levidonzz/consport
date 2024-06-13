from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import User, Sport, Contest


# Create your views here.
def index(request):
    sport_list = get_list_or_404(Sport)
    context = {'sport_list': sport_list}
    return render(request, 'connect/index.html', context)


def sport(request, sport_id):
    sport = get_object_or_404(Sport, pk=sport_id)
    contests = get_list_or_404(Contest, sport=sport)
    context = {
        'sport': sport,
        'contests': contests,
    }
    return render(request, 'connect/sport.html', context)


def contest(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    context = {
        'contest': contest
    }
    return render(request, 'connect/contest.html', context)


def all_user(request):
    user_list = get_list_or_404(User)
    context = {
        'user_list': user_list
    }
    return render(request, 'connect/users.html', context)


def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user': user
    }
    return render(request, 'connect/user.html', context)


def join_contest(request, user_id, contest_id):
    user = get_object_or_404(User, pk=user_id)
    contest = get_object_or_404(Contest, pk=contest_id)
    contest.objects.update()
    context = {
        'user': user,
    }
    return render(request, 'connect/index.html', context)