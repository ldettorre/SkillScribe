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

    def get_category(self):
        return self.category


class Entry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(BehaviouralQuestion, on_delete=models.CASCADE)
    created_on = datetime.datetime.now()
    situation = models.TextField(blank=False)
    task = models.TextField(blank=False)
    action = models.TextField(blank=False)
    result = models.TextField(blank=False)

    def __str__(self):
        return self.question.title

    def get_user_categories(request):
        user_entries = Entry.objects.filter(owner = request.user)
        user_categories = set()
        for i in user_entries:
            user_categories.add(i.question.category.name)
        return user_categories