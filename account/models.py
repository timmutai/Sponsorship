from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



# Create your models here.
class accountManager(BaseUserManager):
    
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('Email is a required')    
        
        user=self.model(
            email=self.normalize_email(email),
        )
 
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):     
                
        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
            )

        user.is_staff=True
        user.is_superuser=True
        user.is_active=True 

        
        user.save(using=self._db)
        return user

class account(AbstractBaseUser,PermissionsMixin):
    
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    date_joined=models.DateField(auto_now_add=True)
    lastLogin=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    is_sponsor=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['password']

    objects=accountManager()


    def __str__(self):
        return str(self.email)

    def has_perm(self,perm, obj=None):
        return self.is_superuser
    def has_module_perm(self, app_label):
            return True
        

   


