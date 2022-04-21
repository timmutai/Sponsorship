from account.models import account
from django.db import models
from account.models import account
from django.db.models.deletion import CASCADE


# Create your models here.

class sponsor(models.Model):
    
    user=models.ForeignKey(account, on_delete=models.CASCADE, unique=True)
    sponsorName=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    country=models.CharField(max_length=100)
    

    def __str__(self):
        return str(self.sponsorName)

 

