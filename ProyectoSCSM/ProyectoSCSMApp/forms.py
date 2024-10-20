from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User # Modelo que utiliza el formulario
        fields = ['username','first_name', 'last_name', 'email','password1','password2'] #campos del formulario
