from django.db import models


class Song(models.Model):
    """
    Class that represents Song object
    fields: name, artist, id, acousticness, danceability, energy, instrumentalness,
    liveness, valence, loudness, speechiness, tempo, key, time_signature, mood
    """
    name = models.CharField('Name', blank=False, max_length=50)
    artists = models.CharField('Artists', blank=False, max_length=50)
    song_id = models.CharField('Id', max_length=100, unique=True)
    acousticness = models.FloatField()
    danceability = models.FloatField()
    energy = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    valence = models.FloatField()
    loudness = models.FloatField()
    speechiness = models.FloatField()
    tempo = models.FloatField()
    key = models.FloatField()
    time_signature = models.FloatField()
    mood = models.CharField('Mood', blank=False, max_length=15)

    def __str__(self) -> str:
        return f'"{self.name}" is a {self.mood} song'

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'
        ordering = ['-name']
