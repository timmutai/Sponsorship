from django.forms import ModelForm
from account.models import account
from student.models import applications
from django.contrib.auth.forms import UserCreationForm

# form 
class studentSchoolForm(ModelForm):
    class Meta:
        model=applications
        exclude=['IdNo','sponsorId','applicationDate','staffApproval','sponsorshipStatus']

class RecomendationForm(ModelForm):
    class Meta:
        model=applications
        fields=('reason_for_application','recomendation','birth_certificate','national_id')
        
