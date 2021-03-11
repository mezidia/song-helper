import spotipy

from unittest import TestCase

from .utils import SpotifyUtils


class TestSpotifyUtils(TestCase):
    def setUp(self) -> None:
        self.util_obj = SpotifyUtils()

    def test_creation(self):
        """Our object must be an instance of SpotifyUtils class"""
        self.assertIsInstance(self.util_obj, SpotifyUtils)

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
