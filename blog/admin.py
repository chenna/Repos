from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time', 'author',)
    
admin.site.register(Article,ArticleAdmin)
