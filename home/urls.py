#new home urls file
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', views.home, name='home-home'),
	path('about/', views.about, name='home-about'),
    
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
