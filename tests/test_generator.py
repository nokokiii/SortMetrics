import unittest

from src.generator import generate_data

class TestGenerator(unittest.TestCase):
    def test_generate_data_length(self):
        self.assertEqual(10, len(generate_data(10, min_value=0, max_value=20)))

    def test_generate_data_low_range(self):
        self.assertLessEqual(0, min(generate_data(10, min_value=0, max_value=20)))

    def test_generate_data_high_range(self):
        self.assertGreaterEqual(20, max(generate_data(10, min_value=0, max_value=20)))
