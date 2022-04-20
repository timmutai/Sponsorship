from django.urls import path
from . import views

urlpatterns = [       
       
       path('studentBioInfo', views.studentBioInfo, name='studentBioInfo'),
       path('StudentSchoolInfo', views.StudentSchoolInfo, name='StudentSchoolInfo'),
       path('recomendation', views.recomendation, name='recomendation'),
       path('profileupdate/<int:id>/',views.profileupdate,name='profileupdate'),
]
