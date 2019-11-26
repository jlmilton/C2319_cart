from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home-home'),
    path('about/', views.about, name='home-about'),
]
