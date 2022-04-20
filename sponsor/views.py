#from account.views import index, register
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SponsorAccountForm
from django.contrib.auth.decorators import login_required
# from .models import applications, sponsor,student
from django.contrib import messages
from django.core.mail import send_mail

# Captures sponsor details

def sponsorInfo (request):
   if request.method=='POST':
      form=SponsorAccountForm(request.POST)
      if form.is_valid():
            
         form.save()
            
         return redirect('login')
        
      return render(request,'sponsor/sponsoraccount.html', {"form": form})
   else:
      form=SponsorAccountForm()
      return render(request,'sponsor/sponsoraccount.html',{'form': form })



