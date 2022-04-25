from account.models import account
from django.db import models
from sponsor.models import sponsor
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save

# Create your models here.

# model to store student details
class student(models.Model):
       
    user=models.OneToOneField(account, on_delete=models.CASCADE)
    first_Name=models.CharField(max_length=200)
    last_Name=models.CharField(max_length=200)
    address=models.CharField(max_length=100)
    phone_No=models.IntegerField()
    email=models.EmailField(unique=True)
    birth_certificate=models.FileField(upload_to='files')
    national_id=models.FileField(upload_to='files')
    school_name=models.CharField(max_length=200 )
    school_address=models.CharField(max_length=200 )
    academic_level=models.CharField(max_length=100 )
    year_of_completion=models.DateField(null=True)
    reason_for_application=models.TextField()
    recomendation=models.FileField(upload_to='recomendation')
    
    

    def __str__(self):
        return str(self.user)


# Model to store student application status
class applications(models.Model):
    
    studentId=models.OneToOneField(student,on_delete=models.CASCADE)
    sponsorId=models.ForeignKey(sponsor,on_delete=models.CASCADE, null=True)
    spplicationDate=models.DateField(auto_now_add=True)
    staffApproval=models.TextField(max_length=20, default='Pending review')
    sponsorshipStatus=models.TextField(max_length=20, default='Awaiting Sponsorship')

    def __str__(self):
        return str(self.studentId)

def CreateApplication (sender, instance, created, **kwargs):
    if created:
        
        applications.objects.create(studentId=instance)
        
post_save.connect(CreateApplication, sender=student)
