import unittest

from csv_ical import convert


class TestConvert(unittest.TestCase):
    def setUp(self):
        self.convert = convert.Convert()

    def test_generate_configs(self):
        self.convert._generate_configs_from_default()
