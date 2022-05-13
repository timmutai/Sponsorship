from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('StudentRegister', views.StudentRegister, name='StudentRegister'),
    path('SponsorRegistration', views.SponsorRegistration, name='SponsorRegistration'),
]