from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import UserProfileForm
from django.views.generic import DetailView
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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
            #
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username , password=password)
            # login(response, user)

        return redirect('/')
    else:
        form = RegisterForm()
        profile_form = UserProfileForm()
    context = {'form' : form, 'profile_form' : profile_form}
    return render(response, 'register/register.html' , context)


# class ProfileView(DetailView):
#         model = UserProfile
#         template_name = 'registration/profilepage.html'

def profile(response):
    args = {'user' : response.user}
    return render (response, 'registration/profile.html' , args)
