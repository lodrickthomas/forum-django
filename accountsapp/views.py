from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from accountsapp.forms import RegistrationForm,EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'accountsapp/index.html')


def about(request):
    return render(request,'accountsapp/about.html')

# @login_required
def profile(request):
    args = {'user':request.user}
    return render(request,'accountsapp/profile.html',args)


def registration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return redirect('/account/')
            # return redirect('/account/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()

    return render(request, 'accountsapp/registration.html', {'form': form})


# @login_required
def edit_profile(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EditProfileForm(request.POST, instance=request.user)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return redirect('/account/profile')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'accountsapp/edit_profile.html', {'form': form})

# @login_required
def change_password(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PasswordChangeForm(data=request.POST, user=request.user)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()


            # keep user sign in after user change password
            update_session_auth_hash(request,form.user)

            # redirect to a new URL:
            return redirect('/account/profile')
        # if data entered not correct then do this...
        else:
            return redirect('/account/change-password')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'accountsapp/change_password.html', {'form': form})