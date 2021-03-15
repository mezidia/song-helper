from unittest import TestCase

from .predict import PredictMood
from .utils import SpotifyUtils


class TestPredictMood(TestCase):
    def setUp(self) -> None:
        self.predict = PredictMood()
        self.spt = SpotifyUtils()
        self.assertIsNotNone(self.predict)
        self.assertIsNotNone(self.spt)
        self.id = '4Km5HrUvYTaSUfiSGPJeQR'

    def test_prepare_data(self):
        """Returned data must be customized"""
        data = self.spt.get_song(self.id)[6:-2]
        expected = [343150.0, 0.927, 0.061, 0.665, 0.0, 0.123, 0.175, -5.313, 0.244, 127.076]
        self.assertIsNotNone(self.predict.prepare_data(data))
        self.assertEqual(self.predict.prepare_data(data), expected)

    def test_prepare_artists(self):
        """Returned string must be without list symbols"""
        data = self.spt.get_song(self.id)[2][1]
        expected = "'Migos', 'Lil Uzi Vert'"
        self.assertIsNotNone(self.predict.prepare_artists(data))
        self.assertEqual(self.predict.prepare_artists(data), expected)

    def test_predict_mood(self):
        """Test the output from function that predicts the mood"""
        output = self.predict.predict_mood(self.id, 'song-helper/data/data_moods.csv')
        expected = "Bad and Boujee (feat. Lil Uzi Vert) by 'Migos', 'Lil Uzi Vert' is a ENERGETIC song"
        self.assertIsNotNone(output)
        self.assertEqual(output, expected)
