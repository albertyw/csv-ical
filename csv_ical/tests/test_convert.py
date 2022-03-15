import datetime
import tempfile
import unittest

from syspath import get_git_root

from csv_ical import convert

EXAMPLE_DIR = get_git_root() / 'examples'
EXAMPLE_ICS = EXAMPLE_DIR / 'arrive.ics'
EXAMPLE_CSV = EXAMPLE_DIR / 'BostonCruiseTerminalSchedule.csv'
CSV_CONFIGS = {
    'HEADER_ROWS_TO_SKIP': 2,
    'CSV_NAME': 3,
    'CSV_START_DATE': 7,
    'CSV_END_DATE': 8,
    'CSV_DESCRIPTION': 6,
    'CSV_LOCATION': 9,
}


class TestConvert(unittest.TestCase):
    def setUp(self) -> None:
        self.convert = convert.Convert()

    def test_generate_configs(self) -> None:
        config = self.convert._generate_configs_from_default()
        self.assertEqual(config['CSV_NAME'], 0)

    def test_generate_configs_override(self) -> None:
        overrides = {
            'CSV_NAME': 5,
        }
        config = self.convert._generate_configs_from_default(overrides)
        self.assertEqual(config['CSV_NAME'], 5)

    def test_read_ical(self) -> None:
        self.convert.read_ical(EXAMPLE_ICS)
        self.assertTrue(self.convert.cal is not None)

    def test_read_csv(self) -> None:
        self.convert.read_csv(EXAMPLE_CSV)
        self.assertNotEqual(self.convert.csv_data, [])

    def test_make_ical(self) -> None:
        self.convert.read_csv(EXAMPLE_CSV)
        self.convert.csv_data = [self.convert.csv_data[0]]
        self.convert.csv_data[0][7] = datetime.datetime.now()
        self.convert.csv_data[0][8] = datetime.datetime.now()
        self.convert.make_ical(CSV_CONFIGS)
        self.assertTrue(self.convert.cal is not None)

    def test_make_csv(self) -> None:
        self.convert.read_ical(EXAMPLE_ICS)
        self.convert.make_csv()
        self.assertNotEqual(self.convert.csv_data, [])

    def test_make_csv_vevent(self) -> None:
        self.convert.read_ical(EXAMPLE_ICS)
        self.convert.cal.subcomponents[0].name = 'asdf'
        self.convert.make_csv()
        self.assertNotEqual(self.convert.csv_data, [])

    def test_make_csv_no_dtstart(self) -> None:
        self.convert.read_ical(EXAMPLE_ICS)
        del self.convert.cal.subcomponents[0]['DTSTART']
        self.convert.make_csv()
        self.assertEqual(self.convert.csv_data[0][1], '')

    def test_make_csv_no_dtend(self) -> None:
        self.convert.read_ical(EXAMPLE_ICS)
        del self.convert.cal.subcomponents[0]['DTEND']
        self.convert.make_csv()
        self.assertEqual(self.convert.csv_data[0][2], '')

    def test_save_ical(self) -> None:
        self.convert.read_ical(EXAMPLE_ICS)
        with tempfile.NamedTemporaryFile() as temp:
            self.convert.save_ical(temp.name)

    def test_save_csv(self) -> None:
        self.convert.read_csv(EXAMPLE_CSV)
        with tempfile.NamedTemporaryFile() as temp:
            self.convert.save_csv(temp.name)
