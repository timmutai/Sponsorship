from django.urls import path
from . import views

urlpatterns = [
    path('applicationList', views.applicationList, name='applicationList'),
    path('StudentDetail/<int:pk>/', views.StudentDetail, name='StudentDetail'),
    path('approve/<int:pk>/', views.approve, name='approve'),
    
    
    
]