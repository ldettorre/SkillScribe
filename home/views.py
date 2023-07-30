from django.shortcuts import render,redirect
from entries.views import questions

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('questions')
    return render(request, 'home/index.html')

