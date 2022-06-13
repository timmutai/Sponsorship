from account.models import account
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save

# Model to store student application status
class applications(models.Model):
    
    idno=models.ForeignKey(account,on_delete=models.CASCADE)    
    school_name=models.CharField(max_length=200 )
    school_address=models.CharField(max_length=200 )
    academic_level=models.CharField(max_length=100 )
    year_of_completion=models.DateField(null=True)
    reason_for_application=models.TextField()
    recomendation=models.FileField(upload_to='recomendation')
    birth_certificate=models.FileField(upload_to='files')
    national_id=models.FileField(upload_to='files')
    sponsor=models.TextField(max_length=200, null=True)
    applicationDate=models.DateField(auto_now_add=True)
    staffapproval=models.TextField(max_length=20, default='Pending review')
    sponsorshipStatus=models.TextField(max_length=20, default='Awaiting Sponsorship')

    def __str__(self):
        return str(self.idno)





