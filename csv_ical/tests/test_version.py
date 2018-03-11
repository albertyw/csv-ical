import unittest

from csv_ical import __version__


class TestVersion(unittest.TestCase):
    def test_version(self):
        self.assertTrue(__version__)
