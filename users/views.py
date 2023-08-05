from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# login and logout are given aliases as they conflict with the view names

def login(request):
    if request.user.is_authenticated:
        return redirect('questions')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print('User logged in.')
            return redirect('questions')
        else:
            print('User not logged in.')
            return redirect('login')
    else:
        return render(request, 'users/login.html')

def logout(request): 
    auth_logout(request)
    print('User logged out')
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('questions')

    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save() 
            auth_login(request,user)
            return redirect('questions')
    else: 
        form = CustomUserCreationForm()
    context = {  
        'form':form  
    }
    return render(request, 'users/register.html', context)
            

def profile(request):
    if request.user.is_authenticated:
        form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'users/profile.html', context)
    else:
        return redirect('login')

def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(data=request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('profile')
        else:
            form = CustomUserChangeForm(instance=user)
    context = {  
        'form':form  
    }
    return render(request, 'users/profile.html',context)