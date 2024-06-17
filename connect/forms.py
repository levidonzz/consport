from django import forms


class Register(forms.Form):
    name = forms.CharField(label='Name', max_length=128)
    test = forms.CharField(label='test', max_length=100)
