import tekore as tk
from .config import Config


class SpotifyUtils:
    """
    Class for making requests to Spotify API
    """
    def __init__(self, client_id=Config.client_id, client_secret=Config.client_secret,
                 redirect_uri=Config.redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        # Credentials to access the Spotify Music Data
        self.app_token = tk.request_client_token(self.client_id, self.client_secret)
        self.spt = tk.Spotify(self.app_token)

    def get_artist(self, artist_id: str):
        """
        Get information about the artist
        :param artist_id: identifier of artist
        :return: information about the artist
        """
        artist = self.spt.artist(artist_id)
        return {
            'id': artist.id,
            'name': artist.name,
            'popularity': artist.popularity,
            'genres': [genre for genre in artist.genres]
        }

    def get_album_songs(self, album_id: str):
        """
        Get songs of the album
        :param album_id: identifier of album
        :return: tracks in album and total number of tracks
        """
        tracks = self.spt.album_tracks(album_id, limit=50)
        return {
            'tracks': tracks.items,
            'total': tracks.total,
        }

    def get_song_meta(self, song_id: str) -> dict:
        """
        Get meta-info about the song
        :param song_id: identifier of song
        :return: Meta-info about song
        """
        info = self.spt.track(song_id)
        return {
            'name': info.name,
            'album': info.album.name,
            'artists': str([artist.name for artist in info.artists]),
            'release_date': info.album.release_date,
            'length': float(info.duration_ms),
            'popularity': float(info.popularity),
            'id': info.id,
        }

    def get_song_analise(self, song_id: str) -> dict:
        """
        Analise the song
        :param song_id: identifier of song
        :return: info after analysing the song
        """
        analise = self.spt.track_audio_analysis(song_id)
        return {
            'bars': analise.bars,
            'beats': analise.beats,
            'sections': analise.sections,
            'segments': analise.segments,
            'tatums': analise.tatums,
        }

    def get_song_features(self, song_id: str) -> dict:
        """
        Get features of song
        :param song_id: identifier of song
        :return: song features
        """
        features = self.spt.track_audio_features(song_id)
        return {
            'acousticness': float(features.acousticness),
            'danceability': float(features.danceability),
            'energy': float(features.energy),
            'instrumentalness': float(features.instrumentalness),
            'liveness': float(features.liveness),
            'valence': float(features.valence),
            'loudness': float(features.loudness),
            'speechiness': float(features.speechiness),
            'tempo': float(features.tempo),
            'key': float(features.key),
            'time_signature': float(features.time_signature),
        }

    def get_song(self, song_id: str) -> list:
        """
        Get all information about song
        :param song_id: identifier of song
        :return: information about song
        """
        meta = self.get_song_meta(song_id)
        features = self.get_song_features(song_id)

        # track = [name, album, artist, song_id, release_date, popularity, length, danceability, acousticness,
        #          energy, instrumentalness, liveness, valence, loudness, speechiness, tempo, key, time_signature]
        # columns = ['name', 'album', 'artist', 'id', 'release_date', 'popularity', 'length', 'danceability',
        #            'acousticness',
        #            'energy', 'instrumentalness',
        #            'liveness', 'valence', 'loudness', 'speechiness', 'tempo', 'key', 'time_signature']
        # return track, columns
        return [*meta.items(), *features.items()]

    def download_albums(self, music_id, artist=False):
        """Download albums"""
        pass

    def download_playlist(self, id_playlist, n_songs):
        """Download playlist"""
        pass
