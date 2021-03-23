from .words_preprocessor import WordPreprocessor
import unittest
from unittest.mock import patch


class TestWordPreprocessor(unittest.TestCase):
    """
    Class for testing WordPreprocessor class
    """
    def setUp(self):
        self.preprocessor = WordPreprocessor()

    # region Equal Tests
    """
    Test if method is working fine
    """

    def test_clean_text_equal_Passing_text(self):
        result = self.preprocessor.clean_text("Passing test")
        expected = "passing test"
        self.assertEqual(result, expected)

    def test_clean_text_not_equal_Passing_text(self):
        result = self.preprocessor.clean_text("Passing test")
        expected = "not passing test"
        self.assertNotEqual(result, expected)

    def test_clean_text_equal_new_text(self):
        result = self.preprocessor.clean_text("new text")
        expected = "new text"
        self.assertEqual(result, expected)

    def test_clean_text_not_equal_new_text(self):
        result = self.preprocessor.clean_text("new text")
        expected = "not new text"
        self.assertNotEqual(result, expected)

    # endregion Equal Tests

    # region Instance Tests
    """
    Test if instances are the same
    """

    def test_instance_PredictMood_predictor(self):
        self.assertIsInstance(self.preprocessor, WordPreprocessor)

    def test_not_instance_PredictMood_predictor(self):
        self.assertNotIsInstance(self.preprocessor, TestWordPreprocessor)

    # endregion Instance Tests

    # region Mock Text Tests
    """
    Test if method is working fine using mocks
    """

    @patch('words_preprocessor.WordPreprocessor.clean_text', return_value="passing test using mock")
    def test_clean_text_equal_mock_Passing_text(self, clean_text):
        result = self.preprocessor.clean_text("Passing test using mock")# 'Passing test using mock not true' to check, that mock is working
        expected = "passing test using mock"
        self.assertEqual(result, expected)

    @patch('words_preprocessor.WordPreprocessor.clean_text', return_value="passing test using mock")
    def test_clean_text_not_equal_mock_Passing_text(self, clean_text):
        result = self.preprocessor.clean_text("Passing test using mock")
        expected = "not passing test using mock"
        self.assertNotEqual(result, expected)

    @patch('words_preprocessor.WordPreprocessor.clean_text', return_value="new text using mock")
    def test_clean_text_equal_mock_new_text(self, clean_text):
        result = self.preprocessor.clean_text("new text using mock")
        expected = "new text using mock"
        self.assertEqual(result, expected)

    @patch('words_preprocessor.WordPreprocessor.clean_text', return_value="passing test using mock")
    def test_clean_text_not_equal_mock_new_text(self, clean_text):
        result = self.preprocessor.clean_text("Passing test using mock")
        expected = "not new text using mock"
        self.assertNotEqual(result, expected)

    #endregion Mock Text Tests

    def tearDown(self):
        del self.preprocessor

if __name__ == '__main__':
    unittest.main()
