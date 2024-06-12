from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import User, Sport, Contest


# Create your views here.
def index(request):
    sport_list = Sport.objects.all()
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
    context = {}
    return render(request, 'connect/contest.html', context)


def all_contest(request):
    contest_list = Contest.objects.all()
    output = ','.join([contest.name for contest in contest_list])
    return HttpResponse(output)


def all_user(request):
    user_list = User.objects.all()
    output = ','.join([user for user in user_list])
    return HttpResponse(output)