from mood_predictors import Predictors
import unittest


class Predictors(unittest.TestCase):
    """
    Class for testing Predictors class
    """
    def setUp(self):
        self.predictor = Predictors()



    def tearDown(self):
        del self.predictor

if __name__ == '__main__':
    unittest.main()
