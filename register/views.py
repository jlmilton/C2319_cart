from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import UserProfileForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        profile_form = UserProfileForm(response.POST)
        if form.is_valid() and profile_form.is_valid():
            # form.save()
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

        return redirect('/')
    else:
        form = RegisterForm()
        profile_form = UserProfileForm()
    context = {'form' : form, 'profile_form' : profile_form}
    return render(response, 'register/register.html' , context)
