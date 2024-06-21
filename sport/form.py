from django import forms


class UserForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=64)
    username = forms.CharField(label='Username', max_length=32)
    password = forms.CharField(label='Password', max_length=64)