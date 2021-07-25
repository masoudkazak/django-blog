from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import Profile
from django.contrib.auth.models import User


class CreateAccountForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class CreateProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {
            'user_name': forms.HiddenInput()
        }
