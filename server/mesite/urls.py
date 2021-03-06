from django.urls import path
from . import views

app_name = 'mesite'

urlpatterns = [
    path('', views.index, name='index'),
]
