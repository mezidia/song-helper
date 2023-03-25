from django.shortcuts import render
from django.http import JsonResponse
from datetime import date
import json
from .forms import MainForm, AddForm
from songhelper import predict, mood_from_words, utils
from .models import Song
from random import randint
from .searcher import search_youtube


year = date.today().year


def index(request):
    song_id = ''
    song_name = ''
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            mood = form.cleaned_data['text']
            data = get_song(request, mood)
            json_data = json.loads(data.content)
            song_id = json_data['song_id']
            song_name = json_data['song']
    context = {
        'song_id': song_id,
        'song_name': song_name,
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
                name = json.loads(data.content)['song']
                result = f'Song "{name}" added as {mood}'
            except Exception as error:
                print(error)
                result = 'Cannot find your song'
    context = {
        'form': AddForm(),
        'year': year,
        'result': result,
    }
    return render(request, 'mesite/add_song.html', context)


def get_song(request, text):
    predictor = mood_from_words.PredictMood()
    mood = predictor.predict(text)[0].capitalize()
    songs = Song.objects.filter(mood=mood)
    if len(songs):
        random_number = randint(0, len(songs)-1)

        song = songs[random_number]

        song_name, link = song.name, search_youtube(song.name)
        print(link)
        data = {
            'mood': text,
            'song': song_name,
            'song_id': link['song_id']
        }
        return JsonResponse(data)
    return JsonResponse({'song_id':''})


def add_song_resp(request, song_id):
    util = utils.SpotifyUtils()

    url_with_data = 'https://raw.githubusercontent.com/mezgoodle/images/master/data_moods.csv'
    predictor = predict.PredictMood()
    mood = predictor.predict_mood(song_id, url_with_data)['mood']

    meta_info = util.get_song_meta(song_id)

    features = util.get_song_features(song_id)
    features['name'] = meta_info['name']
    features['artists'] = meta_info['artists']
    features['song_id'] = song_id
    features['mood'] = mood

    song = Song(**features)
    song.save()

    data = {
        'success': 'true',
        'song': meta_info['name'],
        'mood': mood
    }
    return JsonResponse(data)
