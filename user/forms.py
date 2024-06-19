from django import forms


class UserForm(forms.Form):
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Username', max_length=32)
    password = forms.CharField(label='Password', max_length=64)
