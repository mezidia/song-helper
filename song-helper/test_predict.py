from unittest import TestCase

from .predict import PredictMood
from .utils import SpotifyUtils


class TestPredictMood(TestCase):
    def setUp(self) -> None:
        self.predict = PredictMood()
        self.spt = SpotifyUtils()
        self.assertIsNotNone(self.predict)
        self.assertIsNotNone(self.spt)
        self.id = '2H7PHVdQ3mXqEHXcvclTB0'

    def test_prepare_data(self):
        """Returned data must be customized"""
        data = self.spt.get_song(self.id)[6:-2]
        expected = [379266.0, 0.866, 0.137, 0.73, 0.0, 0.0843, 0.625, -8.201, 0.0767, 118.523]
        self.assertIsNotNone(self.predict.prepare_data(data))
        self.assertEqual(self.predict.prepare_data(data), expected)

    def test_prepare_artists(self):
        """Returned string must be without list symbols"""
        data = self.spt.get_song(self.id)[2][1]
        expected = "'Prince'"
        self.assertIsNotNone(self.predict.prepare_artists(data))
        self.assertEqual(self.predict.prepare_artists(data), expected)

    def test_predict_mood(self):
        """Test the output from function that predicts the mood"""
        output = self.predict.predict_mood(self.id, 'song-helper/data/data_moods.csv')
        expected = "1999 by 'Prince' is a HAPPY song"
        self.assertIsNotNone(output)
        self.assertEqual(output, expected)