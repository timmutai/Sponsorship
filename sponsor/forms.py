
from django.forms import ModelForm
from account.models import account
from .models import sponsor
from django.contrib.auth.forms import UserCreationForm


# class SponsorAccountForm(UserCreationForm):
#     class Meta:
#         model=account
#         fields=['email','is_sponsor']
        
class SponsorAccountForm(ModelForm): 
    class Meta:
        model=sponsor
        exclude=['user',]

