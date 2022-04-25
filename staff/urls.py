from django.urls import path
from . import views

urlpatterns = [
    path('applicationList', views.applicationList, name='applicationList'),
    path('StudentDetail/<int:pk>/', views.StudentDetail, name='StudentDetail'),
    path('StaffApproval/<int:pk>/', views.StaffApproval, name='StaffApproval'),
    
    
    
]