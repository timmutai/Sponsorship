from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import studentSchoolForm, RecomendationForm
from django.contrib.auth.decorators import login_required
from student.models import applications
from django.contrib import messages
from django.core.mail import send_mail
   

# captures student school info
@login_required
def StudentSchoolInfo(request):
   
   
   if request.method =='POST' and request.user.is_authenticated:
      
      form = studentSchoolForm(request.POST,request.FILES)
      if form.is_valid():
                  
         form.instance.studentId = request.user         
         form.save()
                    
         return redirect('index')
      print("form.errors: ", form.errors)
      return render(request,'student/student.html', {"form": form})
   else:
      form= studentSchoolForm()
      return render(request,'student/student.html',{'form':form})




  