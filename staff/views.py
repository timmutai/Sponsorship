from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from pkg_resources import declare_namespace
from student.models import applications
from account.models import account
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

# Retrieves a List of all Applications
@login_required
def applicationList(request):
    if request.method=='GET' and request.user.is_staff:

        students=account.objects.raw("SELECT * FROM account_account  INNER JOIN student_applications on account_account.idno =student_applications.idno_id ")         
        return render(request,'staff/studentlist.html',{'students':students})        

    elif request.method=='GET' and request.user.is_sponsor:

        value='Approved'
        students=account.objects.raw("SELECT * FROM account_account  INNER JOIN student_applications on account_account.idno =student_applications.idno_id WHERE staffapproval=%s",[value])
        application=applications.objects.all()   
        accounts=account.objects.all() 
        # context={'students':application,'accounts':accounts}
        return render(request,'staff/studentlist.html',{'students':students}) 

# retrieves details of a specific student
@login_required
def ApplicationDetail(request,pk):
    if request.method=='GET' and request.user.is_staff:
        id=pk
        studentdetails=account.objects.raw("SELECT * FROM account_account INNER JOIN student_applications on account_account.idno =student_applications.idno_id WHERE  id=%s",[id])        
        return render(request,'staff/studentdetails.html',{'studentdetails':studentdetails})
    elif request.method=='GET' and request.user.is_sponsor:
        
        id=pk
        studentdetails=account.objects.raw("SELECT * FROM account_account INNER JOIN student_applications on account_account.idno =student_applications.idno_id WHERE  id=%s",[id])        
        return render(request,'staff/studentdetails.html',{'studentdetails':studentdetails})
        
# Enables staff to approves applications and send email to student
@login_required
def StaffApproval(request,pk):
    ApplicationApproval=applications.objects.filter(id=pk).first()
    ApplicationApproval.staffapproval='Approved'
    ApplicationApproval.save()

    # #sends email to student if application is approved by a staff
    # student=account.objects.filter(id=pk).first()
    # mail=student.email
#     send_mail(
#       'Spornsorship', # subject
#       'Your application for sponsorship has been approved by a staff, Kindly wait for sponsorship',  # message
#       '', # sender
#       [mail], #receiver
#       fail_silently=False,
#    )
    
    return redirect(applicationList)


