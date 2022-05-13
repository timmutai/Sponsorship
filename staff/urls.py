from django.urls import path
from . import views

urlpatterns = [
    path('applicationList', views.applicationList, name='applicationList'),
    path('ApplicationDetail/<int:pk>', views.ApplicationDetail, name='ApplicationDetail'),
    path('StaffApproval/<int:pk>/', views.StaffApproval, name='StaffApproval'),
    
    
    
]