# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    First_name = forms.CharField(
        required=True, label='Firstname')  
    Last_name = forms.CharField(
        required=True, label='Lastname')  

    class Meta:
        model = User
        fields = ['username', 'email', 'First_name', 'Last_name', 'password1', 'password2']
    
    


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    First_name = forms.CharField()  
    Last_name = forms.CharField()  
    class Meta:
        model = User
        fields = ['username', 'email', 'First_name', 'Last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
