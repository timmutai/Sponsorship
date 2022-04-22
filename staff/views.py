from email import message
from django.shortcuts import redirect, render
from.forms import  staffForm
from django.contrib.auth.decorators import login_required
from student.models import student
from django.http import HttpResponse
# Create your views here.

@login_required

def applicationList(request):
    if request.method=='GET' and request.user.is_staff:

        students=student.objects.all()   
        return render(request,'staff/studentlist.html',{'students':students})
        
        studentdetail=student.objects.filter(id=pk)

    else: 
        message='No details to dispaly'
        return HttpResponse(message)

def StudentDetail(request,pk):
    if request.method=='GET' and request.user.is_staff:
        studentdetails=student.objects.filter(id=pk).first()
        return render(request,'staff/studentdetails.html',{'studentdetail':studentdetails})
        

def approve(request,pk):
    a=student.objects.filter(id=pk).first()
    a.status='Approved'
    a.save()

    return redirect(applicationList)