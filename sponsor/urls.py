from django.urls import path
from . import views

urlpatterns = [  
       
      
       path('SponsorApproval/<int:pk>/',views.SponsorApproval,name='SponsorApproval'),
      
]
