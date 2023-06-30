from django.contrib import admin
from .models import Category, BehaviouralQuestion


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','type',)

class BehaviouralQuestionAdmin(admin.ModelAdmin):
    list_display = ('id','category', 'title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(BehaviouralQuestion, BehaviouralQuestionAdmin)
