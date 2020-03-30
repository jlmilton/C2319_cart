from django.shortcuts import render
from django.http import HttpResponse
from .models import About
from django.contrib import messages


# Create your views here.
def home(request):
    messages.success(request , 'Welcome back')
    storage_1 = messages.get_messages(request)
    return render(request, '../templates/home.html', {'title': 'Home' , 'message_1' : storage_1})


def about(request):
    return render(request, '../templates/about.html', {'title': 'About'})

def forsale(request):
    return render(request, '../templates/forsale.html', {'title': 'For Sale'})
