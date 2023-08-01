from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .form import *

# Create your views here.
def baseview(request):
    return render(request,'base.html')


def indexview(request):
    return render(request,'index.html')

def registerview(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            return redirect('/index/')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'login.html')