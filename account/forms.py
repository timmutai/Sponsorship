from account.models import account
from django import forms
from django.contrib.auth.forms import UserCreationForm


class StudentRegistrationForm(UserCreationForm):
    
    email=forms.EmailField
    

    class Meta:
        model= account
        fields=['firstName','lastName','idno','phone_No','address','email']

class SponsorRegistrationForm(UserCreationForm):

    email=forms.EmailField

    class Meta:
        model=account
        fields=['firstName','lastName','idno','phone_No','address','email']
