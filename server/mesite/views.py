from django.shortcuts import render
from datetime import date
from .forms import MainForm, AddForm

year = date.today().year


def index(request):
    result = ''
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            mood = form.cleaned_data['text']
            # TODO: go to song-helper/mood_from_words.py and get mood
            # mood = predict_mood(text)
            # TODO: go to Songs model and get random song with this mood
            # song = Songs.query(mood)
            # TODO: go to searcher.py and get link
            # link = searcher(song)
            result = mood.capitalize()
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
                # TODO: go to song-helper/predict.py and get mood
                # result = predict_mood(song_id)
                # TODO: go to song-helper/utils.py and get song feature
                # features = get_song_features(song_id)
                # TODO: save new object to model
                # Song.save(features)
                result = f'Song with id "{song_id}" added as Happy'
            except:
                result = 'Cannot find your song'
    context = {
        'form': AddForm(),
        'year': year,
        'result': result,
    }
    return render(request, 'mesite/add_song.html', context)
