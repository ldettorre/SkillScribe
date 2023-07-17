from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
   class Meta:
     model = Entry
     fields = ('situation', 'task', 'action', 'result')
