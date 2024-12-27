from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'description', 'birthday']