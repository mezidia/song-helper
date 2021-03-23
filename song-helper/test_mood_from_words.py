from mood_from_words import PredictMood
import unittest
from unittest.mock import patch


class TestPredictMood(unittest.TestCase):
    """
    Class for testing PredictMood class
    """
    def setUp(self):
        self.predictor = PredictMood()

    # region Not None Tests
    """
    Test if fields are not none
    """

    # def test_field_not_none_nlp(self):
    #     self.assertIsNotNone(self.predictor.nlp)

    # def test_field_not_none_df(self):
    #     self.assertIsNotNone(self.predictor.df)

    # def test_field_not_none_classifier(self):
    #     self.assertIsNotNone(self.predictor.classifier)

    # def test_field_not_none_X(self):
    #     self.assertIsNotNone(self.predictor.X)

    # def test_field_not_none_ylabels(self):
    #     self.assertIsNotNone(self.predictor.ylabels)

    # def test_field_not_none_X_train(self):
    #     self.assertIsNotNone(self.predictor.X_train)

    # def test_field_not_none_X_test(self):
    #     self.assertIsNotNone(self.predictor.X_test)

    # def test_field_not_none_y_train(self):
    #     self.assertIsNotNone(self.predictor.y_train)

    # def test_field_not_none_y_test(self):
    #     self.assertIsNotNone(self.predictor.y_test)

    # def test_field_not_none_pipe_tfid(self):
    #     self.assertIsNotNone(self.predictor.pipe_tfid)

    # endregion Not None Tests

    # region None Tests
    """
    Test if fields are none
    """

    # def test_field_none_nlp(self):
    #     self.predictor.nlp = None
    #     self.assertIsNone(self.predictor.nlp)

    # def test_field_none_df(self):
    #     self.predictor.df = None
    #     self.assertIsNone(self.predictor.df)

    # def test_field_none_classifier(self):
    #     self.predictor.classifier = None
    #     self.assertIsNone(self.predictor.classifier)

    # def test_field_none_X(self):
    #     self.predictor.X = None
    #     self.assertIsNone(self.predictor.X)

    # def test_field_none_ylabels(self):
    #     self.predictor.ylabels = None
    #     self.assertIsNone(self.predictor.ylabels)

    # def test_field_none_X_train(self):
    #     self.predictor.X_train = None
    #     self.assertIsNone(self.predictor.X_train)

    # def test_field_none_X_test(self):
    #     self.predictor.X_test = None
    #     self.assertIsNone(self.predictor.X_test)

    # def test_field_none_y_train(self):
    #     self.predictor.y_train = None
    #     self.assertIsNone(self.predictor.y_train)

    # def test_field_none_y_test(self):
    #     self.predictor.y_test = None
    #     self.assertIsNone(self.predictor.y_test)

    # def test_field_none_pipe_tfid(self):
    #     self.predictor.pipe_tfid = None
    #     self.assertIsNone(self.predictor.pipe_tfid)

    # endregion Not None Tests

    # region Instance Tests
    """
    Test if instances are the same
    """

    # def test_instance_PredictMood_predictor(self):
    #     self.assertIsInstance(self.predictor, PredictMood)

    # def test_not_instance_PredictMood_predictor(self):
    #     self.assertNotIsInstance(self.predictor, TestPredictMood)

    # endregion Instance Tests

    # region Mood Tests
    """
    Test if moods are predicted properly
    """

    # def test_predict_happy(self):
    #     result = self.predictor.predict('I want happy music')
    #     expected = 'HAPPY'
    #     self.assertEqual(result, expected)

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

    # endregion Mood Tests

    # region Mock Mood Tests
    """
    Test if moods are predicted properly using mocks
    """

    @patch('mood_from_words.PredictMood.predict', return_value='HAPPY')
    def test_predict_mock_happy(self, predict):
        result = self.predictor.predict('I want happy music')# 'I want sad music' to check, that mock is working
        expected = 'HAPPY'
        self.assertEqual(result, expected)

    @patch('mood_from_words.PredictMood.predict', return_value='SAD')
    def test_predict_mock_not_happy(self, predict):
        result = self.predictor.predict('I want sad music')
        expected = 'HAPPY'
        self.assertNotEqual(result, expected)

    @patch('mood_from_words.PredictMood.predict', return_value='SAD')
    def test_predict_mock_sad(self, predict):
        result = self.predictor.predict('I want sad music')
        expected = 'SAD'
        self.assertEqual(result, expected)

    @patch('mood_from_words.PredictMood.predict', return_value='ENERGETIC')
    def test_predict_mock_not_sad(self, predict):
        result = self.predictor.predict('I want energetic music')
        expected = 'SAD'
        self.assertNotEqual(result, expected)

    @patch('mood_from_words.PredictMood.predict', return_value='ENERGETIC')
    def test_predict_mock_energetic(self, predict):
        result = self.predictor.predict('I want energetic music')
        expected = 'ENERGETIC'
        self.assertEqual(result, expected)

    @patch('mood_from_words.PredictMood.predict', return_value='CALM')
    def test_predict_mock_not_energetic(self, predict):
        result = self.predictor.predict('I want calm music')
        expected = 'ENERGETIC'
        self.assertNotEqual(result, expected)

    @patch('mood_from_words.PredictMood.predict', return_value='CALM')
    def test_predict_mock_calm(self, predict):
        result = self.predictor.predict('I want calm music')
        expected = 'CALM'
        self.assertEqual(result, expected)

    @patch('mood_from_words.PredictMood.predict', return_value='HAPPY')
    def test_predict_mock_not_calm(self, predict):
        result = self.predictor.predict('I want happy music')
        expected = 'CALM'
        self.assertNotEqual(result, expected)

    # endregion Mock Mood Tests


    def tearDown(self):
        del self.predictor

if __name__ == '__main__':
    unittest.main()
