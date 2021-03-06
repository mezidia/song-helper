from django.contrib import admin
from .models import Mood, Song


@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ('mood',)
    list_filter = ('mood',)
    search_fields = ['mood', ]


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'song_id', 'mood')
    list_filter = ('mood',)
    search_fields = ['name', 'artist']
