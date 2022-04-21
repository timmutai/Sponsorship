
from django.contrib import admin
from django.urls import include,path

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path('', include('account.urls')),
    path('', include('student.urls')),
    path('', include('staff.urls')),
    path('', include('sponsor.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)