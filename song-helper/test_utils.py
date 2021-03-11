import spotipy

from unittest import TestCase

from .utils import SpotifyUtils


class TestSpotifyUtils(TestCase):
    def setUp(self) -> None:
        self.util_obj = SpotifyUtils()
        self.util_obj_1 = SpotifyUtils('test_id', 'test_secret', 'test_uri')

    def test_creation(self):
        """Our object must be an instance of SpotifyUtils class"""
        self.assertIsInstance(self.util_obj, SpotifyUtils)
        self.assertIsInstance(self.util_obj_1, SpotifyUtils)

    def test_default_fields(self):
        """If we do not set params in constructor, they must be set as default. And test their types"""
        self.assertIsNotNone(self.util_obj.spt)
        self.assertIsInstance(self.util_obj.spt, spotipy.Spotify)
        self.assertIsNotNone(self.util_obj.redirect_uri)
        self.assertIsInstance(self.util_obj.redirect_uri, str)
        self.assertIsNotNone(self.util_obj.client_secret)
        self.assertIsInstance(self.util_obj.client_secret, str)
        self.assertIsNotNone(self.util_obj.client_id)
        self.assertIsInstance(self.util_obj.client_id, str)

    def test_custom_fields(self):
        """If we set params in constructor, they must not be set as default. And test their types and values"""
        self.assertIsNotNone(self.util_obj_1.spt)
        self.assertIsInstance(self.util_obj_1.spt, spotipy.Spotify)
        self.assertIsNotNone(self.util_obj_1.redirect_uri)
        self.assertIsInstance(self.util_obj_1.redirect_uri, str)
        self.assertEqual(self.util_obj_1.redirect_uri, 'test_uri')
        self.assertIsNotNone(self.util_obj_1.client_secret)
        self.assertIsInstance(self.util_obj_1.client_secret, str)
        self.assertEqual(self.util_obj_1.client_secret, 'test_secret')
        self.assertIsNotNone(self.util_obj_1.client_id)
        self.assertIsInstance(self.util_obj_1.client_id, str)
        self.assertEqual(self.util_obj_1.client_id, 'test_id')

    def test_get_song_features_method(self):
        """Test getting features from the song"""
        self.assertIsNotNone(self.util_obj.get_songs_features('4iLqG9SeJSnt0cSPICSjxv'))
        self.assertIsNotNone(self.util_obj_1.get_songs_features('4iLqG9SeJSnt0cSPICSjxv'))
        self.assertEqual(len(self.util_obj.get_songs_features('4iLqG9SeJSnt0cSPICSjxv')), 2)
        self.assertIsInstance(self.util_obj.get_songs_features('4iLqG9SeJSnt0cSPICSjxv'), tuple)
        self.assertIsInstance(self.util_obj.get_songs_features('4iLqG9SeJSnt0cSPICSjxv')[0], list)
        self.assertIsInstance(self.util_obj.get_songs_features('4iLqG9SeJSnt0cSPICSjxv')[1], list)


    # def test_get_albums_id(self):
    #     self.fail()
    #
    # def test_get_album_songs_id(self):
    #     self.fail()
    #
    # def test_get_songs_features(self):
    #     self.fail()
    #
    # def test_download_albums(self):
    #     self.fail()
    #
    # def test_download_playlist(self):
    #     self.fail()
