from email import message
from django.contrib.auth import login
from django.shortcuts import render, redirect
from sponsor.models import sponsor
from .forms import SponsorInfoForm, SponsorAccountCreationForm
from django.contrib.auth.decorators import login_required
from account.models import  account
from student.models import applications, student
from staff.views import applicationList
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

    if sponsor.objects.filter(user_id=request.user.id).exists():
      
      prof= sponsor.objects.filter(user=request.user.id).first()
      return render (request,'sponsor/profile.html',{'prof':prof})

    elif request.method=='POST':
      form=SponsorInfoForm(request.POST)
      if form.is_valid():
         form.instance.user = request.user 
         form.save()
            
         return redirect('login')
        
      return render(request,'sponsor/sponsoraccount.html', {"form": form})
    else:
      form=SponsorInfoForm()
      return render(request,'sponsor/sponsoraccount.html',{'form': form })



# Enables Sponsor to choose students to sponsor

def SponsorApproval(request,pk):
    # retrieves the logged in sponsor details
    Sponsor=sponsor.objects.filter(user=request.user).first()

    # updates the sponsor details on applications model
    ApplicationApproval=applications.objects.filter(studentId=pk).first()
    ApplicationApproval.sponsorId=Sponsor
    ApplicationApproval.sponsorshipStatus='Sponsored by :' +Sponsor.sponsorName
    ApplicationApproval.save()

    # #sends email to student if application is approved by a staff
    students=student.objects.filter(id=pk).first() # selects the student bu id
    mail=students.email
    emessa='Your application for sponsorship has been approved by a sponsor,Below are the sponsor details :'
    
    
    send_mail(
      'Spornsorship', # subject
      # message
      f'{emessa},Name :{Sponsor.sponsorName},Email :{Sponsor.email},Phone :{Sponsor.phone},Country :{Sponsor.country}',
      '', # sender
      [mail], #receiver
      fail_silently=False,
   )
    
    return redirect(applicationList)