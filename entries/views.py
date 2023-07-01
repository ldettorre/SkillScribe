from django.shortcuts import render
from .models import Category, BehaviouralQuestion
# Create your views here.

def questions(request):
    categories  = Category.objects.all()
    questions = BehaviouralQuestion.objects.all()
    context ={
        'categories' : categories,
        'questions' : questions,
    }
    return render(request, 'entries/questions.html',context)

