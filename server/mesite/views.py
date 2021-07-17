from django.shortcuts import render
from django.http import JsonResponse
from datetime import date
import json
from .forms import MainForm, AddForm
from songhelper import predict, mood_from_words
from .models import Song
from random import randint
from searcher import search_youtube


year = date.today().year


def index(request):
    result = ''
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            mood = form.cleaned_data['text']
            data = get_song(request, mood)
            link = json.loads(data.content)['link']
            result = link.capitalize()
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
                data = add_song_resp(request, song_id)
                mood = json.loads(data.content)['mood']
                result = f'Song with id "{song_id}" added as {mood}'
            except:
                result = 'Cannot find your song'
    context = {
        'form': AddForm(),
        'year': year,
        'result': result,
    }
    return render(request, 'mesite/add_song.html', context)


def get_song(request, text):
    predictor = mood_from_words.PredictMood()
    mood = predictor.predict(text)

    songs = Song.objects.filter(mood=mood)
    random_number = randint(0, len(songs))
    song = songs[random_number]

    song_name, link = song.name, search_youtube(song.name)
    data = {
        'mood': text,
        'song': song_name,
        'link': link
    }
    return JsonResponse(data)


def add_song_resp(request, song_id):
    # TODO: go to song-helper/predict.py and get mood
    # result = predict_mood(song_id)
    # TODO: go to song-helper/utils.py and get song feature
    # features = get_song_features(song_id)
    # TODO: save new object to model
    # Song.save(features)
    song_name, result = 'Test name', 'Test mood'
    data = {
        'success': 'true',
        'song': song_name,
        'mood': result
    }
    return JsonResponse(data)
