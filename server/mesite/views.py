from django.shortcuts import render
from datetime import date
from .forms import MainForm, AddForm

year = date.today().year


def index(request):
    result = ''
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            result = text.capitalize()
    context = {
        'result': result,
        'form': MainForm(),
        'year': year,
    }
    return render(request, 'mesite/index.html', context)


def add_song(request):
    result = ''
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            song_id = form.cleaned_data['song_id']
            try:
                result = f'Song with id "{song_id}" added as Happy'
            except:
                result = 'Cannot find your song'
    context = {
        'form': AddForm(),
        'year': year,
        'result': result,
    }
    return render(request, 'mesite/add_song.html', context)
