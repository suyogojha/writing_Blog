from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Profile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]