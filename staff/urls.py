from django.urls import path
from . import views

urlpatterns = [
    path('applicationList', views.applicationList, name='applicationList'),
    path('approve/<int:user_id>/', views.approve, name='approve'),
    
    
    
]