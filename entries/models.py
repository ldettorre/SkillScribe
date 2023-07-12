import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class BehaviouralQuestion(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=350)
    helpful_tip = models.CharField(max_length=350, blank=True)

    def __str__(self):
        return self.title

class Entry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(BehaviouralQuestion, on_delete=models.DO_NOTHING)
    created_on = datetime.datetime.now()
    situation = models.CharField(max_length=300)
    task = models.TextField()
    action = models.CharField(max_length=300)
    result = models.CharField(max_length=300)