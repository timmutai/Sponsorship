from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from student.models import student,applications
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

# Retrieves a List of all students
@login_required
def applicationList(request):
    if request.method=='GET' and request.user.is_staff:

        students=student.objects.all()   
        return render(request,'staff/studentlist.html',{'students':students})        

    elif request.method=='GET' and request.user.is_sponsor:
        students=student.objects.all()   
        return render(request,'staff/studentlist.html',{'students':students}) 

# retrieves details of a specific student
def StudentDetail(request,pk):
    if request.method=='GET' and request.user.is_staff:
        studentdetails=student.objects.filter(id=pk).first()
        return render(request,'staff/studentdetails.html',{'studentdetail':studentdetails})
    elif request.method=='GET' and request.user.is_sponsor:
        studentdetails=student.objects.filter(id=pk).first()
        return render(request,'staff/studentdetails.html',{'studentdetail':studentdetails})
        
# Enables staff to approves applications and send email to student
def StaffApproval(request,pk):
    ApplicationApproval=applications.objects.filter(studentId=pk).first()
    ApplicationApproval.staffApproval='Approved'
    ApplicationApproval.save()

    # #sends email to student if application is approved by a staff
    students=student.objects.filter(id=pk).first()
    mail=students.email
    send_mail(
      'Spornsorship', # subject
      'Your application for sponsorship has been approved by a staff, Kindly wait for sponsorship',  # message
      '', # sender
      [mail], #receiver
      fail_silently=False,
   )
    
    return redirect(applicationList)


