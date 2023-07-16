from django.contrib import admin
from .models import Category, BehaviouralQuestion, Entry


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

class BehaviouralQuestionAdmin(admin.ModelAdmin):
    list_display = ('id','category', 'title',)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('id','owner', 'created_on')


admin.site.register(Category, CategoryAdmin)
admin.site.register(BehaviouralQuestion, BehaviouralQuestionAdmin)
admin.site.register(Entry, EntryAdmin)