from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Target, WordList

admin.site.register(Target)
admin.site.register(WordList)
