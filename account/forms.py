from account.models import account
from django import forms
from django.contrib.auth.forms import UserCreationForm


class StudentRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['phone_No'].label = 'Phone No (Example: +254700000000)'
    
    email=forms.EmailField
    
    class Meta:
        model= account
        fields=['firstName','lastName','idno','phone_No','address','country','email']

class SponsorRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SponsorRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['phone_No'].label = 'Phone No (Example: +254700000000)'

    email=forms.EmailField

    class Meta:
        model=account
        fields=['firstName','lastName','idno','phone_No','address','country','email']
