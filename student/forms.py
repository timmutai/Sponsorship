from django.forms import ModelForm
from account.models import account
from .models import student
from django.contrib.auth.forms import UserCreationForm



class studentBioForm(ModelForm):
       
    class Meta:
        model=student

        fields=('first_Name','last_Name','address','phone_No','email','birth_certificate','national_id')

class studentSchoolForm(ModelForm):
    class Meta:
        model=student
        fields=('school_name','school_address','academic_level','year_of_completion')

class RecomendationForm(ModelForm):
    class Meta:
        model=student
        fields=('reason_for_application','recomendation')
        
class ProfileUpdateForm(ModelForm):
    class Meta:
        model=student
        exclude=['user','sponsor']