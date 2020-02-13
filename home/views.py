from django.shortcuts import render
from django.http import HttpResponse
from .models import About

# Create your views here.
def home(request):
    return render(request, '../templates/home.html', {'title': 'Home'})


def about(request):
    return render(request, '../templates/about.html', {'title': 'About'})
