
from django.forms import ModelForm
from account.models import account
from .models import sponsor
from django.contrib.auth.forms import UserCreationForm


class SponsorAccountCreationForm(UserCreationForm):
    class Meta:
        model=account
        fields=['email']
        
class SponsorInfoForm(ModelForm): 
    class Meta:
        model=sponsor
        exclude=['user',]

