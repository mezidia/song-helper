from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from .models import Song
from .forms import MainForm, AddForm
from .searcher import search_youtube


class SongModelTest(TestCase):
    """
    Test Song model
    """

    @classmethod
    def setUpTestData(cls):
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
            mood='Happy',
        )

    def test_song_content(self):
        """
        Test fields on equality and instance of some types
        """
        song = Song.objects.get(id=1)
        self.assertEquals(song.mood, 'Happy')
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

    def test_get_add_song(self):
        """
        Test get method for mesite:add_song
        """
        url = reverse('mesite:add_song')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post_add_song(self):
        """
        Test post method for mesite:add_song
        """
        url = reverse('mesite:add_song')
        response = self.client.post(url, data={'song_id': '0mel2N9Ws9r4yLQn5QE21Y'})
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_get_song(self):
        """
        Test get method for mesite:get_song
        """
        url = reverse('mesite:get_song', kwargs={'text': 'test text'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_add_song_resp(self):
        """
        Test get method for mesite:add_song_resp
        """
        url = reverse('mesite:add_song_resp', kwargs={'song_id': '0mel2N9Ws9r4yLQn5QE21Y'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)



class MainFormTests(TestCase):
    """
    Test app forms
    """

    def test_valid_input_form(self):
        """
        Test valid form
        """
        data = {'text': 'test-text'}
        form = MainForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_input_form(self):
        """
        Test invalid form
        """
        data = {}
        form = MainForm(data=data)
        self.assertFalse(form.is_valid())


class AddFormTests(TestCase):
    """
    Test app forms
    """

    def test_valid_input_form(self):
        """
        Test valid form
        """
        data = {'song_id': 'test-text'}
        form = AddForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_input_form(self):
        """
        Test invalid form
        """
        data = {}
        form = AddForm(data=data)
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
        self.assertIsInstance(result1['title'], str)
        self.assertIsNotNone(result1['views'])
        self.assertTrue(result1['views'].endswith('views'))
        self.assertIsNotNone(result2['duration'])
        self.assertIsInstance(result2['duration'], str)
        self.assertIsNotNone(result2['song_id'])
        self.assertIsInstance(result2['song_id'], str)
