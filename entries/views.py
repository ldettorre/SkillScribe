from datetime import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, BehaviouralQuestion, Entry
from django.contrib.auth.decorators import login_required
from .forms import EntryForm

# Create your views here.

def questions(request):
    categories  = Category.objects.all()
    questions = BehaviouralQuestion.objects.all()
    context ={
        'categories' : categories,
        'questions' : questions,
    }
    return render(request, 'entries/questions.html',context)


@login_required(login_url="/login/")
def add_entry(request, question_id):
    question = get_object_or_404(BehaviouralQuestion, id=question_id)
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            Entry = form.save(commit=False)
            Entry.owner = request.user
            Entry.question = question
            Entry.save()
            return redirect('questions')
    else:
        form = EntryForm()
        context ={
            'form' : form,
            'question' : question,
        }
        return render(request, 'entries/add_entry.html',context)
