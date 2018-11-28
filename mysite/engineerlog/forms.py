from django import forms
from .models import AppUser, Profile

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('displayname', 'icon', 'profile_sentence')

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = AppUser
        fields = ("username","email")