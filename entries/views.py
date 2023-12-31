from datetime import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, BehaviouralQuestion, Entry
from django.contrib.auth.decorators import login_required
from .forms import EntryForm

# Create your views here.

def questions(request):
    categories  = Category.objects.all().order_by("name")
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


@login_required(login_url="/login/")
def get_entries(request):
    # Filter the entries retrieved that only match the logged in user.
    # Filter the entries retrieved that only match the logged in user.
    entries = Entry.objects.filter(owner = request.user).order_by('question')
    user_categories = Entry.get_user_categories(request)
    selected_category = request.GET.get('category')
    if selected_category in user_categories:
        entries = entries.filter(question__category__name=selected_category)
    
    context = {
        'entries' : entries,
        'user_categories' : user_categories,
    }
    return render(request, 'entries/my_entries.html',context)


@login_required(login_url="/login/")
def edit_entry(request, entry_id):
    # Get required entry by id.
    entry = get_object_or_404(Entry, id=entry_id)
    
    # If the logged in user is not the entry owner, they're
    # redirected as to not allow them to edit someone elses entry. 
    if request.user != entry.owner:
        return redirect('get_entries')

    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('get_entries')
    else:
        context = {'form': EntryForm(instance=entry), 'entry': entry}
        return render(request, 'entries/edit.html',context)
    

@login_required(login_url="/login/")
def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    if request.user != entry.owner:
        return redirect('get_entries')
    else:
        entry.delete()
        return redirect('get_entries')