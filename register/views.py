from django.shortcuts import render, redirect, get_object_or_404
from .forms import(
    RegisterForm,
    UserProfileForm,
    EditProfileForm,
    EditProfileFormCustme,
    RemoveUser,
)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash , get_user_model , login
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages




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
            login(response , user)

            subject = "Welcome to C-2319 (College Market)"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            message = """Welcome to College Market, the best way to buy and sell stuff online to other students, staff and faclty members."""
            send_mail(subject , message , email_from , recipient_list)

            return redirect('/')
            #messages.success(response , 'Your profile has been created.')
    else:
        form = RegisterForm()
        profile_form = UserProfileForm()
    context = {'form' : form, 'profile_form' : profile_form}
    return render(response, 'register/register.html' , context)

def edit_profile(response , pk=None):
    current_user = response.user.userprofile.pk
    user_edit = get_object_or_404(UserProfile, pk=current_user)

    if response.method == 'POST':
        form_e = EditProfileForm(response.POST , instance=response.user)
        profile_form_e = UserProfileForm(response.POST , instance=user_edit)
        if form_e.is_valid() and profile_form_e.is_valid():
            user = form_e.save()
            profile = profile_form_e.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('/account/profile')
    else:
        form_e = EditProfileForm(instance=response.user)
        profile_form_e = UserProfileForm(instance=user_edit)
    context = {'form_e' : form_e , 'profile_form_e' : profile_form_e , 'user_edit' : user_edit}
    return render(response, 'registration/edit_profile.html' , context)

def remove_user(response , pk=None):
    if response.method == 'POST':
        item = get_object_or_404(User , pk=pk)
        rem = User.objects.get(username=form.cleaned_data['username'])
        User.delete()
        return redirect('/post/')

    else:
        form = RemoveUser()
    context = {'form': form}
    return render(response, 'registration/remove_user.html', context)



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
    storage = messages.get_messages(response)
    args = {'user' : response.user , 'message' : storage}
    return render (response, 'registration/profile.html' , args)
