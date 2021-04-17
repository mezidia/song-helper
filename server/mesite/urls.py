from django.urls import path
from . import views

app_name = 'mesite'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-song', views.add_song, name='add_song'),
]
