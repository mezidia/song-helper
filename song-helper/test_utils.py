import tekore as tk
import os

from unittest import TestCase

from .utils import SpotifyUtils
from .fake_server import FakeServer


class TestSpotifyUtils(TestCase):
    def setUp(self) -> None:
        self.fs = FakeServer(spt=SpotifyUtils())
        self.util_obj = SpotifyUtils()
        self.util_obj_1 = SpotifyUtils(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'), os.getenv('REDIRECT_URI'))
        self.id = '1fipvP2zmef6vN2IwXfJhY'
        self.id_1 = '6l7lX8hJXVIUyPrTaabpqk'
        self.album_id = '4GRRGsQBwwd2kKaEXZqVNd'
        self.album_id_1 = '5f6Eu9QtujgGggq5qbbycV'
        self.artist_id = '4dwdTW1Lfiq0cM8nBAqIIz'
        self.artist_id_1 = '10exVja0key0uqUkk6LJRT'

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
        song_features = self.fs.get_song_features(self.id)
        song_features_1 = self.fs.get_song_features(self.id_1)
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

    def test_get_song_meta(self):
        """Test getting meta info from the song"""
        song_info = self.util_obj.get_song_meta(self.id_1)
        song_info_1 = self.util_obj_1.get_song_meta(self.id)
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
        """Test analysing the song"""
        song_analise = self.util_obj.get_song_analise(self.id_1)
        song_analise_1 = self.util_obj_1.get_song_analise(self.id)
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
        """Test getting the song"""
        song = self.util_obj.get_song(self.id_1)
        song_1 = self.util_obj_1.get_song(self.id)
        self.assertIsNotNone(song)
        self.assertIsNotNone(song_1)
        self.assertEqual(len(song), 18)
        self.assertEqual(len(song_1), 18)
        self.assertIsInstance(song, list)
        self.assertIsInstance(song_1, list)
        self.assertIsNotNone(song[0])
        self.assertIsInstance(song[0], tuple)
        self.assertIsNotNone(song_1[-1])
        self.assertIsInstance(song_1[-1], tuple)
        self.assertEqual(song[0][0], 'name')
        self.assertEqual(song_1[-1][0], 'time_signature')

    def test_download_albums(self):
        self.skipTest('Not ready')

    def test_download_playlist(self):
        self.skipTest('Not ready')

    def test_get_album_songs(self):
        """Test get songs from album"""
        songs = self.util_obj.get_album_songs(self.album_id)
        songs_1 = self.util_obj_1.get_album_songs(self.album_id_1)
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

    def test_get_artist(self):
        """Test getting the artist"""
        artist = self.util_obj.get_artist(self.artist_id)
        artist_1 = self.util_obj_1.get_artist(self.artist_id_1)
        self.assertIsNotNone(artist)
        self.assertIsNotNone(artist_1)
        self.assertEqual(len(artist), 4)
        self.assertEqual(len(artist_1), 4)
        self.assertIsInstance(artist, dict)
        self.assertIsInstance(artist_1, dict)
        self.assertIsNotNone(artist['id'])
        self.assertIsInstance(artist['id'], str)
        self.assertIsNotNone(artist['popularity'])
        self.assertIsInstance(artist['popularity'], int)
        self.assertIsNotNone(artist_1['name'])
        self.assertIsInstance(artist_1['name'], str)
        self.assertIsNotNone(artist_1['genres'])
        self.assertIsInstance(artist_1['genres'], list)
        self.assertIsNotNone(artist['genres'][0])
        self.assertIsInstance(artist_1['genres'][0], str)

    def tearDown(self) -> None:
        del self.util_obj
        del self.util_obj_1
        del self.id
        del self.id_1
        del self.album_id
        del self.album_id_1
        del self.artist_id
        del self.artist_id_1
