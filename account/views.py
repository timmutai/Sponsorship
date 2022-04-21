from django.contrib.auth import login
from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models import  account
from.forms import UserRegistration
from django.contrib.auth.decorators import login_required 



#landing page
@login_required
def index(request):
    return render(request,'index.html')

# user registration function
def register (request):
    if request.method=='POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            account.is_active=False
            form.save()
            
            return redirect('login')
        print("form.errors: ", form.errors)
        return render(request,'account/registration.html', {"form": form})
    else:
        form=UserRegistration()
        return render(request,'account/registration.html',{'form': form })

