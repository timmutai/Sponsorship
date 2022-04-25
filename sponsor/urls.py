from django.urls import path
from . import views

urlpatterns = [  
       
       path('sponsorInfo',views.sponsorInfo,name='sponsorInfo'),
       path('SponsorAccountCreation',views.SponsorAccountCreation,name='SponsorAccountCreation'),
       path('SponsorApproval/<int:pk>/',views.SponsorApproval,name='SponsorApproval'),
      
]
