from django.shortcuts import render
from django.http import HttpResponse
from .models import About
# Create your views here.
def home(request):
	return render(request, '../templates/home_page/home.html', {'title': 'Home_page'})

def about(request):
	return render(request = request,
				  template_name='../templates/home_page/about.html',
				  context = {'about': About.objects.all})
