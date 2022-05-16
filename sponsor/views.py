from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.models import  account
from student.models import applications
from staff.views import applicationList
from django.core.mail import send_mail
from django.http import HttpResponse



def SponsorApproval(request,pk):
    # retrieves the logged in sponsor details
    

    # updates the sponsor details on applications model
    ApplicationApproval=applications.objects.filter(id=pk).first()
    ApplicationApproval.sponsor=request.user.firstName
    ApplicationApproval.sponsorshipStatus='Sponsored'
    
    ApplicationApproval.save()

    # #sends email to student if application is approved by a staff
    studentmail=account.objects.raw("SELECT * FROM account_account INNER JOIN student_applications on account_account.idno =student_applications.idno_id WHERE  id=%s",[pk]) 
    
    for x in studentmail:
      mail=x.email
      emessage='Your application for sponsorship has been approved by a sponsor,Below are the sponsor details :'
    
      try:
        send_mail(
          'Spornsorship', # subject
          # message
          f'{emessage},Name :{request.user.firstName},Email :{request.user.email},Phone :{request.user.phone_No},Country :{request.user.country}',
          '', # sender
          [mail], #receiver
          fail_silently=False,
      
       )
        return redirect(applicationList)
        
      except:
        return HttpResponse('An error occured, please try again')
    