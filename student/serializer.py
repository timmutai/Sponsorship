from rest_framework import serializers
from account.models import account
from student.models import applications
# from django.contrib.auth.forms import UserCreationForm

# form 
class studentSchoolSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(studentSchoolSerializer, self).__init__(*args, **kwargs)
        self.fields['year_of_completion'].label = 'Year of completion (yyyy-mm-dd)'
    class Meta:
        model=applications
        exclude=['sponsor','applicationDate','staffapproval','sponsorshipStatus']


        
