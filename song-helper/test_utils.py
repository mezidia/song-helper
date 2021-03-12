import tekore as tk
import os

from unittest import TestCase

from .utils import SpotifyUtils


class TestSpotifyUtils(TestCase):
    def setUp(self) -> None:
        self.util_obj = SpotifyUtils()
        self.util_obj_1 = SpotifyUtils(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'), os.getenv('REDIRECT_URI'))

    def test_creation(self):
        """Our object must be an instance of SpotifyUtils class"""
        self.assertIsInstance(self.util_obj, SpotifyUtils)
        self.assertIsInstance(self.util_obj_1, SpotifyUtils)

    def test_default_fields(self):
        """If we do not set params in constructor, they must be set as default. And test their types"""
        self.assertIsNotNone(self.util_obj.spt)
        self.assertIsInstance(self.util_obj.spt, tk.Spotify)
        self.assertIsNotNone(self.util_obj.redirect_uri)
        self.assertIsInstance(self.util_obj.redirect_uri, str)
        self.assertIsNotNone(self.util_obj.client_secret)
        self.assertIsInstance(self.util_obj.client_secret, str)
        self.assertIsNotNone(self.util_obj.client_id)
        self.assertIsInstance(self.util_obj.client_id, str)

    def test_custom_fields(self):
        """If we set params in constructor, they must not be set as default. And test their types and values"""
        self.assertIsNotNone(self.util_obj_1.spt)
        self.assertIsInstance(self.util_obj_1.spt, tk.Spotify)
        self.assertIsNotNone(self.util_obj_1.redirect_uri)
        self.assertIsInstance(self.util_obj_1.redirect_uri, str)
        self.assertEqual(self.util_obj_1.redirect_uri, os.getenv('REDIRECT_URI'))
        self.assertIsNotNone(self.util_obj_1.client_secret)
        self.assertIsInstance(self.util_obj_1.client_secret, str)
        self.assertEqual(self.util_obj_1.client_secret, os.getenv('CLIENT_SECRET'))
        self.assertIsNotNone(self.util_obj_1.client_id)
        self.assertIsInstance(self.util_obj_1.client_id, str)
        self.assertEqual(self.util_obj_1.client_id, os.getenv('CLIENT_ID'))

    def test_get_song_features_method(self):
        """Test getting features from the song"""
        song_features = self.util_obj.get_song_features('1fipvP2zmef6vN2IwXfJhY')
        song_features_1 = self.util_obj_1.get_song_features('6l7lX8hJXVIUyPrTaabpqk')
        self.assertIsNotNone(song_features)
        self.assertIsNotNone(song_features_1)
        self.assertEqual(len(song_features), 11)
        self.assertEqual(len(song_features_1), 11)
        self.assertIsInstance(song_features, dict)
        self.assertIsInstance(song_features_1, dict)
        self.assertIsNotNone(song_features['acousticness'])
        self.assertIsNotNone(song_features['energy'])
        self.assertIsNotNone(song_features['liveness'])
        self.assertIsNotNone(song_features['loudness'])
        self.assertIsNotNone(song_features['tempo'])
        self.assertIsNotNone(song_features['time_signature'])
        self.assertIsNotNone(song_features_1['danceability'])
        self.assertIsNotNone(song_features_1['instrumentalness'])
        self.assertIsNotNone(song_features_1['valence'])
        self.assertIsNotNone(song_features_1['speechiness'])
        self.assertIsNotNone(song_features_1['key'])

    def get_song_meta(self):
        """Test getting meta info from the song"""
        song_info = self.util_obj.get_song_meta('6l7lX8hJXVIUyPrTaabpqk')
        song_info_1 = self.util_obj_1.get_song_meta('1fipvP2zmef6vN2IwXfJhY')
        self.assertIsNotNone(song_info)
        self.assertIsNotNone(song_info_1)
        self.assertEqual(len(song_info), 7)
        self.assertEqual(len(song_info_1), 7)
        self.assertIsInstance(song_info, dict)
        self.assertIsInstance(song_info_1, dict)
        self.assertIsNotNone(song_info['name'])
        self.assertIsInstance(song_info['name'], str)
        self.assertIsNotNone(song_info['artists'])
        self.assertIsInstance(song_info['artists'], str)
        self.assertIsNotNone(song_info['length'])
        self.assertIsNotNone(song_info['id'])
        self.assertIsInstance(song_info['id'], str)
        self.assertIsNotNone(song_info_1['album'])
        self.assertIsInstance(song_info_1['album'], str)
        self.assertIsNotNone(song_info_1['release_date'])
        self.assertIsInstance(song_info_1['release_date'], str)
        self.assertIsNotNone(song_info_1['popularity'])

    def test_get_albums_id(self):
        self.skipTest('Not ready')

    def test_get_album_songs_id(self):
        self.skipTest('Not ready')

    def test_get_song_analise(self):
        song_analise = self.util_obj.get_song_analise('6l7lX8hJXVIUyPrTaabpqk')
        song_analise_1 = self.util_obj_1.get_song_analise('1fipvP2zmef6vN2IwXfJhY')
        self.assertIsNotNone(song_analise)
        self.assertIsNotNone(song_analise_1)
        self.assertEqual(len(song_analise), 5)
        self.assertEqual(len(song_analise_1), 5)
        self.assertIsInstance(song_analise, dict)
        self.assertIsInstance(song_analise_1, dict)
        self.assertIsNotNone(song_analise['bars'])
        self.assertIsInstance(song_analise['bars'], tk.model.ModelList)
        self.assertIsNotNone(song_analise['sections'])
        self.assertIsInstance(song_analise['sections'], tk.model.ModelList)
        self.assertIsNotNone(song_analise['tatums'])
        self.assertIsInstance(song_analise['tatums'], tk.model.ModelList)
        self.assertIsNotNone(song_analise_1['beats'])
        self.assertIsInstance(song_analise_1['beats'], tk.model.ModelList)
        self.assertIsNotNone(song_analise_1['segments'])
        self.assertIsInstance(song_analise_1['segments'], tk.model.ModelList)

    def test_get_song(self):
        self.skipTest('Not ready')

    def test_download_albums(self):
        self.skipTest('Not ready')

    def test_download_playlist(self):
        self.skipTest('Not ready')

    def test_get_album_songs(self):
        songs = self.util_obj.get_album_songs('4GRRGsQBwwd2kKaEXZqVNd')
        songs_1 = self.util_obj_1.get_album_songs('5f6Eu9QtujgGggq5qbbycV')
        self.assertIsNotNone(songs)
        self.assertIsNotNone(songs_1)
        self.assertEqual(len(songs), 2)
        self.assertEqual(len(songs_1), 2)
        self.assertIsInstance(songs, dict)
        self.assertIsInstance(songs_1, dict)
        self.assertIsNotNone(songs['tracks'])
        self.assertIsInstance(songs['tracks'], tk.model.ModelList)
        self.assertIsNotNone(songs_1['tracks'])
        self.assertIsInstance(songs_1['tracks'], tk.model.ModelList)
        self.assertIsNotNone(songs['total'])
        self.assertIsInstance(songs['total'], int)
        self.assertIsNotNone(songs_1['total'])
        self.assertIsInstance(songs_1['total'], int)

    def tearDown(self) -> None:
        del self.util_obj
        del self.util_obj_1
