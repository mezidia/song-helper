from django.contrib import admin
from .models import Song


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'artists', 'song_id', 'mood')
    list_filter = ('mood',)
    search_fields = ['name', 'artists']
