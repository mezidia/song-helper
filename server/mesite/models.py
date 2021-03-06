from django.db import models


class Mood(models.Model):
    """
    Class that represents Mood characteristic of song
    fields: mood
    """
    MOODS = (
        ('H', 'Happy'),
        ('E', 'Energetic'),
        ('C', 'Calm'),
        ('S', 'Sad'),
    )
    mood = models.CharField(max_length=1, choices=MOODS, blank=False)

    def __str__(self) -> str:
        return self.mood

    class Meta:
        verbose_name = 'Mood'
        verbose_name_plural = 'Moods'


class Song(models.Model):
    """
    Class that represents Song object
    fields: name, artist, id, acousticness, danceability, energy, instrumentalness,
    liveness, valence, loudness, speechiness, tempo, key, time_signature, mood
    """
    name = models.CharField('Name', blank=False, max_length=40)
    artist = models.CharField('Artists', blank=False, max_length=20)
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
    key = models.IntegerField()
    time_signature = models.IntegerField()
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'"{self.name}" is a {self.mood} song'

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'
        ordering = ['-name']
