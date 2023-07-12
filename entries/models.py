from django.db import models

# Create your models here.
class Category(models.Model):
    type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.type

class BehaviouralQuestion(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=350)
    helpful_tip = models.CharField(max_length=350, blank=True)

    def __str__(self):
        return self.title