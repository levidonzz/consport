from django import forms


class Register(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    email = forms.EmailField(label='Email')
    gender = forms.CharField()

    
