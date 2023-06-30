from django.urls import path
from . import views

urlpatterns=[
    path('', views.entries, name='entries'),
]