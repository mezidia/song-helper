from django.urls import path
from . import views

app_name = 'mesite'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-song', views.add_song, name='add_song'),
    path('get-song/<str:text>', views.get_song, name='get_song'),
    path('add-song-resp/<str:song_id>', views.get_song, name='add_song_resp')
]
