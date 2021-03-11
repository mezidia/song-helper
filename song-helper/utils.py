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

    def get_albums_id(self, ids: str):
        """Get albums id"""
        pass

    def get_album_songs_id(self, ids: str):
        """Get id of song in album"""
        pass

    def get_song_meta(self, ids: str) -> dict:
        info = self.spt.track(ids)
        return {
            'name': info.name,
            'album': info.album.name,
            'artists': [artist.name for artist in info.artists],
            'release_date': info.album.release_date,
            'length': info.duration_ms,
            'popularity': info.popularity,
            'id': info.id,
        }

    def get_song_analise(self, ids: str):
        pass

    def get_song_features(self, ids: str) -> dict:
        features = self.spt.track_audio_features(ids)
        return {
            'acousticness': features.acousticness,
            'danceability': features.danceability,
            'energy': features.energy,
            'instrumentalness': features.instrumentalness,
            'liveness': features.liveness,
            'valence': features.valence,
            'loudness': features.loudness,
            'speechiness': features.speechiness,
            'tempo': features.tempo,
            'key': features.key,
            'time_signature': features.time_signature,
        }

    def get_song(self, ids: str) -> list:
        """Get features of song"""
        meta = self.get_song_meta(ids)
        features = self.get_song_features(ids)

        # track = [name, album, artist, ids, release_date, popularity, length, danceability, acousticness,
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
