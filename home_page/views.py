from django.shortcuts import render
from django.http import HttpResponse
from .models import About


def home(request):
    return render(request, '../templates/home_page/home.html', {'title': 'Home'})


def about(request):
    return render(request, '../templates/home_page/about.html', {'title': 'About'}, {'about': About.objects.all})
