from email import message
import re
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import Http404, HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import ContestForm, SignInForm, SignUpForm
from .models import Sport, Contest, CustomUser, create_user_avatar


def index(request):
    user_list = CustomUser.objects.all()
    sport_list = Sport.objects.all()
    context = {
        'user_list': user_list,
        'sport_list': sport_list,
    }
    return render(request, 'sport/index.html', context)


# ---------- Contest ----------
def sport_detail(request, sport_id):
    try:
        sport = get_object_or_404(Sport, pk=sport_id)
        contest_list = get_list_or_404(Contest, sport=sport)
        context = {
            'sport': sport,
            'contest_list': contest_list,
        }
        return render(request, 'sport/sport_detail.html', context)
    except Http404:
        return render(request, 'sport/create_contest.html')



def contest_detail(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)
    return render(request, 'sport/contest_detail.html', {'contest': contest})


def join_contest(request, contest_id):
    user = request.user
    contest = get_object_or_404(Contest, id=contest_id)

    if request.method == 'POST':
        if contest.participants.count() >= contest.max_participants:
            messages.error(request, 'This contest is already fully')
        elif user in contest.participants.all():
            messages.error(request, 'You are already a participant in this contest.')
        else:
            contest.participants.add(user)
            messages.success(request, 'You have successfully joined the contest')
    return redirect('sport:contest_detail', contest_id=contest_id)


def unjoin(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)
    user = request.user
    if request.method == 'POST':
        if user in contest.participants.all():
            contest.participants.remove(user)
            messages.success(request, 'You are already cancel this contest.')
        else:
            messages.error(request, 'You have not join this contest')
    return redirect('sport:contest_detail', contest_id=contest_id)


@login_required
def create_contest(request):
    if request.method == 'POST':
        form = ContestForm(request.POST)
        if form.is_valid():
            contest = form.save(commit=False)
            contest.creator = request.user
            contest.save()
            contest.participants.add(request.user)
            form.save_m2m()
            messages.success(request, 'Contest created successfully.')
            return redirect('sport:contest_detail', contest_id=contest.id)
    else:
        form = ContestForm()
    return render(request, 'sport/create_contest.html', {'form': form})


@login_required
def cancel_contest(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)

    if request.user != contest.creator:
        messages.error(request, "You don't have permission to cancel this contest.")
        return redirect('sport:contest_detail', contest_id=contest.id)
    if request.method == 'POST':       
        # Store the sport_id before deleting the contest
        sport_id = contest.sport.id
        # Delete the contest
        contest.delete()
        messages.success(request, "Contest has been successfully cancelled.")
        return redirect('sport:sport_detail', sport_id=sport_id)
    
    return redirect('sport:contest_detail', contest_id=contest_id)

    
# ---------- User ----------
def user_list(request):
    user_list = CustomUser.objects.all()
    context = {
        'user_list': user_list,
    }
    return render(request, 'sport/user_list.html', context)


def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    context = {
        'user': user,
    }
    return render(request, 'sport/user_detail.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = get_object_or_404(CustomUser, username=username)
            login(request, user)
            return redirect('sport:index')
        else:
            return render(request, 'sport/sign_in.html')
    else:
        form = SignInForm()
        return render(request, 'sport/sign_in.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            create_user_avatar(user, True)
            login(request, user)
            messages.success(request, 'Sign Up success, You are automatically logged in.')
            return redirect('sport:index')
    else:
        form = SignUpForm()
    return render(request, 'sport/sign_up.html', {'form': form})
    

def sign_out(request):
    logout(request)
    return redirect('sport:index')