from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from entries.views import questions
# login and logout are given aliases as they conflict with the view names

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print("User logged in.")
            return redirect('questions')
        else:
            print("User not logged in.")
            return redirect('login')
    else:
        return render(request, 'users/login.html')

def logout(request): 
    auth_logout(request)
    print('User logged out')
    return redirect('questions')


def register(request):
    if request.method == 'POST':
        print('Registration Attempt')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        
        if password1 == password2:
            print('Passwords match')
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                print("Username already taken.")
                return redirect('register')
            # Check if the email is already taken
            elif User.objects.filter(email=email).exists():
                print("Email already registered.")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, 
                last_name=last_name, 
                username=username, email=email,
                password=password1)
                user.save()
                print("User registered.")
                auth_login(request,user)
                print("User now logged in after new registration")
                return redirect('profile')
                
        else:
            print('Passwords dont match')
            return redirect('/')
    else:
        return render(request, 'users/register.html')


def profile(request):
    return render(request, 'users/profile.html')