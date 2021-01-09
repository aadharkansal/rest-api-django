from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class customer_signup(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}),required=True,max_length=30)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'}),required=True,max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),required=True,max_length=30)
    
    class Meta:
        model = User
        fields=('name','email','password')

class nursery_signup(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}),required=True,max_length=30)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'}),required=True,max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),required=True,max_length=30)
    
    class Meta:
        model = User
        fields=('name','email','password')

class UserLoginForm(forms.Form):
	username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),required=True,max_length=30)
	password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),required=True,max_length=30)