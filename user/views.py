from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UserForm


# Create your views here.
def users(request):
    context = None
    return render(request, 'user/user_list.html', context)


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('user/success.html')