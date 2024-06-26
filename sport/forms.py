from django import forms
from django.forms.widgets import DateTimeInput

from .models import Contest


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