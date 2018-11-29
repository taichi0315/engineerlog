from django import forms
from .models import AppUser, Post
from django.forms.widgets import NumberInput

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = AppUser
        fields = ('displayname', 'icon', 'profile_sentence')

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = AppUser
        fields = ("username","email", "displayname")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("duration", "comment")
        widgets = {
            'duration': NumberInput(attrs={'type':'range', 'step':'5'})
        }