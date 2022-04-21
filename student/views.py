from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import studentBioForm, studentSchoolForm,RecomendationForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from student.models import applications,student
from django.contrib import messages
from django.core.mail import send_mail


# captures student bio information and updates student information
    
@login_required
def studentBioInfo(request): 
   
   if student.objects.filter(user_id=request.user.id).exists():
      
      prof= student.objects.filter(user=request.user.id).first()
      return render (request,'student/profile.html',{'prof':prof})

      
   else:
      if not request.user.is_staff:

         if request.method =='POST' and request.user.is_authenticated:
      
            form = studentBioForm(request.POST, request.FILES)
            if form.is_valid():
               form.instance.user = request.user
               form.save()

            
               return redirect('StudentSchoolInfo')
               
            return render(request,'student/student.html', {"form": form})
         else:
            form= studentBioForm()
            return render(request,'student/student.html',{'form':form})

      else:
         
         return render(request,'index.html ')

# captures student school info
@login_required
def StudentSchoolInfo(request):
   
   
   if request.method =='POST' and request.user.is_authenticated:
      
      q=student.objects.filter(user=request.user).first()
      form = studentSchoolForm(request.POST,request.FILES,instance=q)
      if form.is_valid():
                  
         form.instance.user = request.user
         form.save()
                    
         return redirect('recomendation')
      print("form.errors: ", form.errors)
      return render(request,'student/student.html', {"form": form})
   else:
      form= studentSchoolForm()
      return render(request,'student/student.html',{'form':form})

# captures reasons for application and recommandation of the student 
@login_required
def recomendation(request):
   
   if request.method =='POST' and request.user.is_authenticated:
      
      q=student.objects.filter(user=request.user).first()
      form = RecomendationForm(request.POST,request.FILES,instance=q)
      if form.is_valid():
                  
         form.instance.user = request.user
         form.save()
         
         return redirect('index')
      print("form.errors: ", form.errors)
      return render(request,'student/school.html', {"form": form})
   else:
      form= RecomendationForm()
      return render(request,'student/student.html',{'form':form})




def profileupdate(request,id):
   profile=student.objects.filter(user_id=id).first()
   form=ProfileUpdateForm(instance=profile)  
   if request.method =='POST':
         
      form=ProfileUpdateForm(request.POST, request.FILES,instance=profile)     
      if form.is_valid():
         
         form.save()
      return redirect(studentBioInfo)

   return render(request,'student/profileupdate.html',{'form':form})

  