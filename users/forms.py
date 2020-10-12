from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()  #adds extra EmailField to the Built-in Django-Forms 
    class Meta:
        model = User        
        fields = ['username', 'email', 'password1', 'password2']       # Pass the required fields 