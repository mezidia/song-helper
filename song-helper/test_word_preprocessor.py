from words_preprocessor import WordPreprocessor
import unittest


class TestWordPreprocessor(unittest.TestCase):
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

    def tearDown(self):
        del self.preprocessor

if __name__ == '__main__':
    unittest.main()
