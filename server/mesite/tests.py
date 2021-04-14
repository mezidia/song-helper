from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from .models import Mood, Song
from .forms import InputForm
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


class ViewsTests(TestCase):
    """
    Test app views
    """
    def test_get_index(self):
        """
        Test get method for mesite:index
        """
        url = reverse('mesite:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_index(self):
        """
        Test post method for mesite:index
        """
        url = reverse('mesite:index')
        response = self.client.post(url, data={'text': 'test-case'})
        self.assertEqual(response.status_code, HTTPStatus.OK)


class FormsTests(TestCase):
    """
    Test app forms
    """
    def test_valid_input_form(self):
        """
        Test valid form
        """
        data = {'text': 'test-text'}
        form = InputForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_input_form(self):
        """
        Test invalid form
        """
        data = {}
        form = InputForm(data=data)
        self.assertFalse(form.is_valid())


class SearcherTest(TestCase):
    """
    Test search on YouTube
    """
    def test_searcher(self):
        """
        Test the function output
        """
        str_to_search = 'python'
        params1 = {'limit': 1}
        params2 = {'limit': 3}
        result1 = search_youtube(str_to_search, params1)
        result2 = search_youtube(str_to_search, params2)
        self.assertIsNotNone(result1)
        self.assertIsNotNone(result2)
        self.assertIsInstance(result1, dict)
        self.assertIsInstance(result2, dict)
        self.assertIsNotNone(result1['title'])
        self.assertEqual(result1['title'], 'Learn Python - Full Course for Beginners [Tutorial]')
        self.assertIsNotNone(result1['views'])
        self.assertTrue(result1['views'].endswith('views'))
        self.assertIsNotNone(result2['duration'])
        self.assertEqual(result2['duration'], '4:26:52')
        self.assertIsNotNone(result2['link'])
        self.assertEqual(result2['link'], 'https://www.youtube.com/watch?v=rfscVS0vtbw')
