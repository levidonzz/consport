from operator import truediv
from django import forms
from django.forms.widgets import DateTimeInput
from django.contrib.auth.forms import UserCreationForm

from .models import Contest, CustomUser


class ContestForm(forms.ModelForm):
    start_date = forms.DateTimeField(
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    end_date = forms.DateTimeField(
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Contest
        fields = ['name', 'sport', 'description', 'start_date', 'end_date', 'max_participants']


class SignInForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')