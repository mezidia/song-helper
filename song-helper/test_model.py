from unittest import TestCase

from .model import make_model


class TestModel(TestCase):
    def test_make_model(self):
        """Test creation the keras model"""
        model = make_model()
        expected_name = 'sequential'
        expected_units = 8
        expected_units_1 = 4
        expected_layer_name = 'dense'
        expected_layer_name_1 = 'dense_1'
        self.assertEqual(model.name, expected_name)
        self.assertEqual(len(model.layers), 2)
        self.assertEqual(model.layers[0].units, expected_units)
        self.assertEqual(model.layers[1].units, expected_units_1)
        self.assertEqual(model.layers[0].name, expected_layer_name)
        self.assertEqual(model.layers[1].name, expected_layer_name_1)
