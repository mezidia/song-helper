from django.contrib import admin
from .models import Mood, Song

@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ('mood',)
    list_filter = ('mood',)
    search_fields = ['mood',]