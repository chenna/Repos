from django.contrib import admin
from .models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name','age',)
    
admin.site.register(Person,PersonAdmin)