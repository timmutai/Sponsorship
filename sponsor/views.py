from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SponsorInfoForm, SponsorAccountCreationForm
from django.contrib.auth.decorators import login_required
from account.models import  account
from django.contrib import messages
from django.core.mail import send_mail

# Captures sponsor details

def SponsorAccountCreation (request):
    if request.method=='POST':
        form=SponsorAccountCreationForm(request.POST)
        if form.is_valid():
            form.instance.is_sponsor=True
            form.save()
            
            return redirect('login')
        print("form.errors: ", form.errors)
        return render(request,'account/registration.html', {"form": form})
    else:
        form=SponsorAccountCreationForm()
        return render(request,'account/registration.html',{'form': form })



def sponsorInfo (request):
   if request.method=='POST':
      form=SponsorInfoForm(request.POST)
      if form.is_valid():
         form.instance.user = request.user 
         form.save()
            
         return redirect('login')
        
      return render(request,'sponsor/sponsoraccount.html', {"form": form})
   else:
      form=SponsorInfoForm()
      return render(request,'sponsor/sponsoraccount.html',{'form': form })



