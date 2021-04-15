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
    context = {
        'form': AddForm(),
        'year': year,
    }
    return render(request, 'mesite/add_song.html', context)
