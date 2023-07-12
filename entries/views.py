from django.shortcuts import render, redirect, get_object_or_404
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


def add_entry(request, question_id):
    question = get_object_or_404(BehaviouralQuestion, id=question_id)
    context ={
        'question' : question,
    }
    return render(request, 'entries/add_entry.html',context)
