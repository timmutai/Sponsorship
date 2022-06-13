from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_view
urlpatterns = [              
       
       path('StudentSchoolInfo', views.StudentSchoolInfo.as_view(), name='StudentSchoolInfo'),
       path('login', auth_view.obtain_auth_token),
      
]
