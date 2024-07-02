import os
from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from . import forms
# from .forms import UserRegisterForm
from .forms import RegistrationForm, LoginForm, ProfileForm
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Profile, Restaraunt

# Create your views here.


def agreement(request):
    return render(request, "agreement.html")


def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginForm()
    return render(request, "login.html", {'form': form})


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            Profile.objects.create(user=user)
            user.save()

            # Redirect to a success page
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def index(request):
    name='Askaneli'
    names = list(Restaraunt.objects.all().values_list('name', flat=True))
    current_rest = Restaraunt.objects.get(name=name)
    other_rest = Restaraunt.objects.exclude(name=name)
    return render(request, "askaneli.html", {'restaraunt': current_rest, 'other_rests': other_rest})


def changerest(request):
    if request.method == 'POST':

        name = request.POST.get('rest_name')
        print(name)
        return index(request, name)


def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return render(request, "profile.html", {'profile': profile})
    except Profile.DoesNotExist:
        return HttpResponseRedirect(reverse('profile_edit'))


def profile_edit(request):
    try:
        profile = Profile.objects.get(user=request.user)
        exImg = profile.image.path
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                os.remove(exImg)
                profile.save()
                return HttpResponseRedirect(reverse('profile'))
        else:
            form = ProfileForm(instance=profile)
    except Profile.DoesNotExist:
        # If the profile does not exist, create a new one
        profile = Profile(user=request.user)
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                profile.save()
                return HttpResponseRedirect(reverse('profile'))
        else:
            form = ProfileForm(instance=profile)

    return render(request, "profile_edit.html", {'form': form, 'profile': profile})

def poll(request):
    return render(request, "poll.html")


