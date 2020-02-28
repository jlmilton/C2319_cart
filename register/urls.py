from . import views
from .views import ProfileView
from django.urls import path


urlpatterns = [
    path('profile_page', ProfileView.as_view(), name='profile_page'),
    ]
