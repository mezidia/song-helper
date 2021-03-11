from unittest import TestCase

from .utils import SpotifyUtils


class TestSpotifyUtils(TestCase):
    def test_creation(self):
        util = SpotifyUtils()
        self.assertIsInstance(util, SpotifyUtils)

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
