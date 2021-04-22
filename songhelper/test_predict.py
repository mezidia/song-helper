from unittest import TestCase

from .predict import PredictMood
from .utils import SpotifyUtils
from .fake_server import FakeServer


class TestPredictMood(TestCase):
    def setUp(self) -> None:
        self.fs = FakeServer(spt=SpotifyUtils(), pt=PredictMood())
        self.predict = PredictMood()
        self.spt = SpotifyUtils()
        self.assertIsNotNone(self.predict)
        self.assertIsNotNone(self.spt)
        self.id = '2H7PHVdQ3mXqEHXcvclTB0'
        self.url_with_data = 'https://raw.githubusercontent.com/mezgoodle/images/master/data_moods.csv'

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
        output = self.fs.get_song_with_mood(self.id, self.url_with_data)
        expected_name = '1999'
        expected_artist = '\'Prince\''
        expected_mood = 'Happy'
        self.assertIsNotNone(output)
        self.assertIsInstance(output, dict)
        self.assertEqual(output['name'], expected_name)
        self.assertEqual(output['artists'], expected_artist)
        self.assertEqual(output['mood'], expected_mood)

    def tearDown(self) -> None:
        del self.predict
        del self.spt
        del self.id
