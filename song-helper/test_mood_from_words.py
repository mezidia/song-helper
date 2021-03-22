from unittest import TestCase

from .mood_from_words import PredictMood


class TestPredictMood(TestCase):
    def setUp(self):
        self.predictor = PredictMood()

    def test_fields(self):
        self.assertIsNotNone(self.predictor.nlp)
        # self.assertIsInstance(self.predictor, PredictMood)
        # self.assertEqual(self.predictor.nlp, 'something')

    def test_predict(self):
        result = self.predictor.predict('something')
        expected = 'something'
        self.assertEqual(result, expected)
        # self.assertIsInstance(result, list)

    def tearDown(self):
        del self.predictor
