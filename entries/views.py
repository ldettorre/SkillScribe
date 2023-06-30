from django.shortcuts import render

# Create your views here.

def entries(request):
    return render(request, 'entries/entries.html')

