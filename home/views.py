from django.shortcuts import render
from django.http import HttpResponse
from .models import About

# Create your views here.	

def home(request):
	return render(request, 'home/home.html', {'title': 'Home'})
	
def about(request):
	return render(request = request,
				  template_name='home/about.html',
				  context = {'about': About.objects.all})

