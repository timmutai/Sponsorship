from django.forms import ModelForm
from account.models import account
from student.models import applications
from django.contrib.auth.forms import UserCreationForm

# form 
class studentSchoolForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(studentSchoolForm, self).__init__(*args, **kwargs)
        self.fields['year_of_completion'].label = 'Year of completion (yyyy-mm-dd)'
    class Meta:
        model=applications
        exclude=['idno','sponsor','applicationDate','staffapproval','sponsorshipStatus']

class RecomendationForm(ModelForm):
    class Meta:
        model=applications
        fields=('reason_for_application','recomendation','birth_certificate','national_id')
        
