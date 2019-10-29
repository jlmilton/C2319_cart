from django.shortcuts import render

# Create your views here.	

members = [
	{
		'name':			'Corey',
		'content':		'Senior at the University of South Carolina working on a BS in Computer Science. \n I have an Associates degree in Mechanical Engineering from Midlands Technical College.'
	},
	{
		'name':			'Erik',
		'content':		'Hey, my name is Erik, and Im a junior in Computer Science.'
	},
	{
		'name':			'Itay',
		'content':		'Hello, my name is Itay Goldfaden and I am a senior'
	},
	{
		'name':			'James',
		'content':		'Hey this james testing.'
	},
	{
		'name':			'Matt',
		'content':		'Hello  my name is matt and I am a senior CIS major.'
	}
]

def home(request):
	return render(request, 'home/home.html', {'title': 'Home Page'})
	
def about(request):
	context = {
		'members': members
	}
	return render(request, 'home/about.html', context)

