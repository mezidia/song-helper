from unittest import TestCase

from .model import make_model


class TestModel(TestCase):
    def setUp(self) -> None:
        self.model = make_model()

    def test_make_model(self):
        """Test creation the keras model"""
        expected_name = 'sequential'
        expected_units = 8
        expected_units_1 = 4
        expected_layer_name = 'dense'
        self.assertTrue(self.model.name.startswith(expected_name))
        self.assertEqual(len(self.model.layers), 2)
        self.assertEqual(self.model.layers[0].units, expected_units)
        self.assertEqual(self.model.layers[1].units, expected_units_1)
        self.assertTrue(self.model.layers[0].name.startswith(expected_layer_name))
        self.assertTrue(self.model.layers[1].name.startswith(expected_layer_name))

    def tearDown(self) -> None:
        del self.model
