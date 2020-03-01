from django.shortcuts import render, redirect
from .forms import(
    RegisterForm,
    UserProfileForm,
    EditProfileForm,
    EditProfileFormCustme,
)
from django.views.generic import DetailView
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


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


def edit_profile(response):
    if response.method == 'POST':
        form = EditProfileForm(response.POST , instance=response.user)
        profile_form = EditProfileFormCustme(response.POST , instance=response.user)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=response.user)
        profile_form = EditProfileFormCustme(instance=response.user)
        context = {'form' : form , 'profile_form' : profile_form}
        return render(response, 'registration/edit_profile.html' , context)

def change_password(response):
    if response.method == 'POST':
        form = PasswordChangeForm(data=response.POST, user=response.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(response , form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/-change-password')
    else:
        form = PasswordChangeForm(user=response.user)
        context = {'form' : form}
        return render(response, 'registration/change_password.html', context)




def view_profile(response):
    args = {'user' : response.user}
    return render (response, 'registration/profile.html' , args)
