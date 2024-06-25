from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import ContestForm
from .models import Sport


def index(request):
    user_list = User.objects.all()
    sport_list = Sport.objects.all()
    context = {
        'user_list': user_list,
        'sport_list': sport_list,
    }
    return render(request, 'sport/index.html', context)


# ---------- Contest ----------
def sport_detail(request, sport_id):
    sport = get_object_or_404(Sport, pk=sport_id)
    context = {
        'sport': sport,
    }
    return render(request, 'sport/sport_detail.html', context)


@login_required
def create_contest(request):
    if request.method == 'POST':
        form = ContestForm(request.POST)
        if form.is_valid():
            contest = form.save(commit=False)
            contest.creator = request.user
            contest.save()
            return render(request, 'sport/contest_detail.html', {'contest': contest})
    else:
        form = ContestForm()
    return render(request, 'sport/create_contest.html', {'form': form})

    
# ---------- User ----------
def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sport:index')
        else:
            messages.error(request, 'Invalid email or password')
            return HttpResponse('Invalid email or password')
    else:
        return render(request, 'sport/sign_in.html')


def sign_up(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = True
        user.save()
        messages.success(request, 'Sign Up success, You are automatically logged in.')
        login(request, user)
        return render(request, 'sport/sign_in.html')
    else:
        return render(request, 'sport/sign_up.html')
    

def sign_out(request):
    logout(request)
    return render(request, 'sport/index.html')