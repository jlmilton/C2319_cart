from django.shortcuts import render
from django.http import HttpResponse
from .models import About
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, '../templates/home.html', {'title': 'Home'})

def about(request):
    return render(request, '../templates/about.html', {'title': 'About'})

def milestone_17(request):
    return render(request, '../templates/milestone_17.html', {'title': 'Milestone 17'})

def forsale(request):
    return render(request, '../templates/forsale.html', {'title': 'For Sale'})
