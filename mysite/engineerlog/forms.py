from django import forms
from .models import AppUser

from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = AppUser
        fields = ('displayname', 'icon', 'profile_sentence')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)