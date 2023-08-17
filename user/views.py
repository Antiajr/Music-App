from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import customCreationForm
from .models import Profiles

# Create your views here.


def contact(request):
    contacts = Profiles.objects.all()
    content = {'contacts': contacts}

    return render(request, 'users/contact.html',content)

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username dose not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password is incorrect')
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'user was successful logout')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = customCreationForm()

    if request.method == 'POST':
        form = customCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'user created successfully')
            return redirect('login')
        else:
            messages.error(request, 'An Error has occurred during registration')
    content = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', content)