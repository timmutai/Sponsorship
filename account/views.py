from django.shortcuts import render
from django.contrib.auth import login
from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models import  account
from.forms import StudentRegistrationForm,SponsorRegistrationForm
from django.contrib.auth.decorators import login_required 




#landing page
@login_required
def index(request):
    return render(request,'index.html')

# Student registration function
def StudentRegister (request):
    if request.method=='POST':
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.instance.is_student=True
            form.save()
            
            return redirect('login')
        print("form.errors: ", form.errors)
        return render(request,'account/registration.html', {"form": form})
    else:
        form=StudentRegistrationForm()
        return render(request,'account/registration.html',{'form': form })

# Sponsor registration function
def SponsorRegistration (request):
    if request.method=='POST':
        form=SponsorRegistrationForm(request.POST)
        if form.is_valid():
            form.instance.is_sponsor=True
            form.save()
            
            return redirect('login')
        print("form.errors: ", form.errors)
        return render(request,'account/registration.html', {"form": form})
    else:
        form=SponsorRegistrationForm()
        return render(request,'account/registration.html',{'form': form })