from account.models import account
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegistration(UserCreationForm):
    
    email=forms.EmailField
    

    class Meta:
        model= account
        fields=['email',]

