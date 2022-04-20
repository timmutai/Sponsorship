from django import forms
from django.forms import ModelForm
from account.models import account
from django.contrib.auth.forms import UserCreationForm
# from sponsor.models import student


class staffForm(UserCreationForm):
    email=forms.EmailField
    

    class Meta:
        model= account
        fields=['email','firstName','lastName']

