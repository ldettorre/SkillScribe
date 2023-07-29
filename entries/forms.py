from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
   class Meta:
     model = Entry
     fields = ('situation', 'task', 'action', 'result')

     widgets = {
      'situation' : forms.Textarea(attrs={'rows': 5,'placeholder': 'Give context on the situation. Explain what was happening or what was the core issue arising.','maxlength': '400'}),
      'task' : forms.Textarea(attrs={'rows': 5,'placeholder': 'Elaborate on what was the problem at hand. What needed to be resolved and what was the disired end-goal or outcome?','maxlength': '400'}),
      'action' : forms.Textarea(attrs={'rows': 10,'placeholder': 'Now is the time to share what you did in response to the situation at hand and task faced. Go into detail bout what you planned, what you attempted, who you communicated and collaborated with? Be sure to share why you performed these steps.','maxlength': '1000'}),
      'result' : forms.Textarea(attrs={'rows': 10,'placeholder': 'After all was said and done, what was the outcome? How did it compare to the intial goal? Was it successful? If not, why? What lessons did you learn and what would you have done differently?','maxlength': '1000'}),
     }

