from django.test import TestCase
from .models import Mood, Song
from .searcher import search_youtube


class MoodModelTest(TestCase):
    """
    Test Mood model
    """
    @classmethod
    def setUpTestData(cls):
        Mood.objects.create(
            mood='Happy',
        )

    def test_mood_content(self):
        """
        Test only one field
        """
        mood = Mood.objects.get(id=1)
        self.assertEquals(mood.mood, 'Happy')


class SongModelTest(TestCase):
    """
    Test Song model
    """
    @classmethod
    def setUpTestData(cls):
        Mood.objects.create(
            mood='Happy',
        )
        mood = Mood.objects.get(id=1)

        Song.objects.create(
            name='Test name',
            artists='Test artist',
            song_id='12312dadav!231',
            acousticness=1.1,
            danceability=3123.321,
            energy=0.000,
            instrumentalness=-1323.1,
            liveness=1.0,
            valence=1.,
            loudness=123.3,
            speechiness=3123.123,
            tempo=123.1,
            key=3123.0,
            time_signature=0.0,
            mood=mood,
        )

    def test_song_content(self):
        """
        Test fields on equality and instance of some types
        """
        song = Song.objects.get(id=1)
        self.assertEquals(song.mood, Mood.objects.get(id=1))
        self.assertIsInstance(song.song_id, str)
        self.assertEquals(song.name, 'Test name')
        self.assertIsInstance(song.energy, float)
        self.assertEquals(song.liveness, 1.)
        self.assertIsInstance(song.key, float)
        self.assertEquals(song.time_signature, 0)


class SearcherTest(TestCase):
    """
    Test search on YouTube
    """
    def test_searcher(self):
        """
        Test the function output
        """
        str_to_search = 'python'
        params = {'limit': 1}
        params_1 = {'limit': 3}
        result = search_youtube(str_to_search, params)
        result_1 = search_youtube(str_to_search, params_1)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result_1)
        self.assertIsInstance(result, dict)
        self.assertIsInstance(result_1, dict)
        self.assertIsNotNone(result['title'])
        self.assertEqual(result['title'], 'Learn Python - Full Course for Beginners [Tutorial]')
        self.assertIsNotNone(result['views'])
        self.assertEqual(result['views'], '22M views')
        self.assertIsNotNone(result_1['duration'])
        self.assertEqual(result_1['duration'], '4:26:52')
        self.assertIsNotNone(result_1['link'])
        self.assertEqual(result_1['link'], 'https://www.youtube.com/watch?v=rfscVS0vtbw')

