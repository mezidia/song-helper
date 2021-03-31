from .utils import SpotifyUtils
from .predict import PredictMood


class FakeServer:
    """
    This fake implements the requests from server-side interface.
    This interface is also used by the real implementation.
    This is used only for testing.
    """
    def __init__(self, spt: SpotifyUtils = None, pt: PredictMood = None) -> None:
        self.spt = spt
        self.pt = pt

    def get_song_with_mood(self, song_id, path) -> dict:
        """
        Django makes request to script to identify song mood
        :param song_id: identifier from Spotify
        :param path: path to dataset
        :return: dictionary with the name of song and mood
        """
        song_with_mood = self.pt.predict_mood(song_id, path)
        return song_with_mood

    def get_song_features(self, song_id) -> dict:
        """
        Django makes request to script to get features of song
        :param song_id: identifier from Spotify
        :return: dictionary with song features
        """
        features = self.spt.get_song_features(song_id)
        return features
