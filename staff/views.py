from django.shortcuts import redirect, render
from.forms import  staffForm
from django.contrib.auth.decorators import login_required
from student.models import student
# Create your views here.

@login_required

def applicationList(request):
    students=student.objects.all()
    

    return render(request,'staff/studentlist.html',{'students':students})

def approve(request,user_id):
    a=student.objects.filter(user_id=user_id).first()
    a.status='Approved'
    a.save()

    return redirect(applicationList)