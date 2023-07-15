from django.urls import path
from . import views

urlpatterns=[
    path('', views.questions, name='questions'),
    path('<int:question_id>', views.add_entry, name='add_entry'),
    path('my_entries', views.get_entries, name='get_entries'),
    path('edit/<int:entry_id>', views.edit_entry, name='edit_entry'),
]