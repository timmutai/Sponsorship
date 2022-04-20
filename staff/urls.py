from django.urls import path
from . import views

urlpatterns = [
    path('staffregister', views.staffregister, name='staffregister'),
    path('applicationList', views.applicationList, name='applicationList'),
    path('approve/<int:user_id>/', views.approve, name='approve'),
    
    
    
]