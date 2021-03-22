from unittest import TestCase

from mood_from_words import PredictMood
import unittest


class TestPredictMood(TestCase):
    def setUp(self):
        self.predictor = PredictMood()

    def test_field_not_none_nlp(self):
        self.assertIsNotNone(self.predictor.nlp)
        # self.assertIsInstance(self.predictor, PredictMood)
        # self.assertEqual(self.predictor.nlp, 'something')

    def test_field_not_none_df(self):
        self.assertIsNotNone(self.predictor.df)

    def test_field_not_none_classifier(self):
        self.assertIsNotNone(self.predictor.classifier)

    def test_field_not_none_X(self):
        self.assertIsNotNone(self.predictor.X)

    def test_field_not_none_ylabels(self):
        self.assertIsNotNone(self.predictor.ylabels)

    def test_field_not_none_X_train(self):
        self.assertIsNotNone(self.predictor.X_train)

    def test_field_not_none_X_test(self):
        self.assertIsNotNone(self.predictor.X_test)

    def test_field_not_none_y_train(self):
        self.assertIsNotNone(self.predictor.y_train)

    def test_field_not_none_y_test(self):
        self.assertIsNotNone(self.predictor.y_test)

    # def test_predict_happy(self):
    #     result = self.predictor.predict('I want happy music')
    #     expected = 'HAPPY'
    #     self.assertEqual(result, expected)
    #     # self.assertIsInstance(result, list)

    # def test_predict_not_happy(self):
    #     result = self.predictor.predict('I want sad music')
    #     expected = 'HAPPY'
    #     self.assertNotEqual(result, expected)

    # def test_predict_sad(self):
    #     result = self.predictor.predict('I want sad music')
    #     expected = 'SAD'
    #     self.assertEqual(result, expected)

    # def test_predict_not_sad(self):
    #     result = self.predictor.predict('I want energetic music')
    #     expected = 'SAD'
    #     self.assertNotEqual(result, expected)

    # def test_predict_energetic(self):
    #     result = self.predictor.predict('I want energetic music')
    #     expected = 'ENERGETIC'
    #     self.assertEqual(result, expected)
    #     # self.assertIsInstance(result, list)

    # def test_predict_not_energetic(self):
    #     result = self.predictor.predict('I want calm music')
    #     expected = 'ENERGETIC'
    #     self.assertNotEqual(result, expected)

    # def test_predict_calm(self):
    #     result = self.predictor.predict('I want calm music')
    #     expected = 'CALM'
    #     self.assertEqual(result, expected)

    # def test_predict_not_calm(self):
    #     result = self.predictor.predict('I want happy music')
    #     expected = 'CALM'
    #     self.assertNotEqual(result, expected)

    def tearDown(self):
        del self.predictor

if __name__ == '__main__':
    unittest.main()