from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.models import  account
from student.models import applications
from staff.views import applicationList
from django.core.mail import send_mail



def SponsorApproval(request,pk):
    # retrieves the logged in sponsor details
    Sponsor=account.objects.filter(idno=request.user.idno).first()

    # updates the sponsor details on applications model
    ApplicationApproval=applications.objects.filter(id=pk).first()
    ApplicationApproval.sponsor=request.user.firstName
    ApplicationApproval.sponsorshipStatus='Sponsored'
    
    ApplicationApproval.save()

    # #sends email to student if application is approved by a staff
  #   students=account.objects.filter(id=pk).first() # selects the student bu id
  #   mail=students.email
  #   emessage='Your application for sponsorship has been approved by a sponsor,Below are the sponsor details :'
    
    
  #   send_mail(
  #     'Spornsorship', # subject
  #     # message
  #     f'{emessage},Name :{Sponsor.firstName},Email :{Sponsor.email},Phone :{Sponsor.phone_No},Country :{Sponsor.country}',
  #     '', # sender
  #     [mail], #receiver
  #     fail_silently=False,
  #  )
    
    return redirect(applicationList)