from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from cineMatch.movies.urls import index
from django.contrib.auth.models import User

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {
                'error': 'Username OR password is incorrect'
            })

    return render(request, 'registration/login.html')

def signup(request):
    #TODO
    return render(request, 'registration/signup.html')


def logout_user(request):
    logout(request)
    return redirect('index')
