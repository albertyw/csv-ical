import datetime
import tempfile
import unittest

from icalendar import Calendar
from syspath import get_git_root

from csv_ical import convert

EXAMPLE_DIR = get_git_root() / 'examples'
EXAMPLE_ICS = EXAMPLE_DIR / 'example.ics'
EXAMPLE_CSV = EXAMPLE_DIR / 'example.csv'
CSV_CONFIGS: convert.Config = {
    'HEADER_ROWS_TO_SKIP': 0,
    'TIMEZONE': 'Europe/Madrid',
    'CSV_NAME': 0,
    'CSV_START_DATE': 1,
    'CSV_END_DATE': 2,
    'CSV_DESCRIPTION': 3,
    'CSV_LOCATION': 4,
    'CSV_DELIMITER': ',',
}


class TestExample(unittest.TestCase):
    def test_example_ics_crlf(self) -> None:
        with open(EXAMPLE_ICS, 'rb') as f:
            content = f.read()
        lf_count = content.count(b'\n')
        crlf_count = content.count(b'\r\n')
        self.assertGreater(crlf_count, 0)
        self.assertEqual(lf_count, crlf_count)


class TestConvert(unittest.TestCase):
    def setUp(self) -> None:
        self.convert = convert.Convert()

    def test_generate_configs(self) -> None:
        config = self.convert._generate_configs_from_default()
        self.assertEqual(config['CSV_NAME'], 0)

    def test_generate_configs_override(self) -> None:
        overrides: convert.ConfigOverrides = {
            'CSV_NAME': 5,
        } # type: ignore
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
        self.convert.csv_data[0][1] = datetime.datetime.now()
        self.convert.csv_data[0][2] = datetime.datetime.now()
        self.convert.make_ical(CSV_CONFIGS)
        self.assertTrue(self.convert.cal is not None)

    def test_make_csv(self) -> None:
        self.convert.read_ical(EXAMPLE_ICS)
        self.convert.make_csv()
        self.assertNotEqual(self.convert.csv_data, [])

    def test_make_ical_all_day_with_timezone(self) -> None:
        start = datetime.date(2026, 9, 22)
        end = datetime.date(2026, 9, 23)
        self.convert.csv_data = [['All day', start, end, '', '']]

        calendar = self.convert.make_ical(CSV_CONFIGS)
        parsed = Calendar.from_ical(calendar.to_ical())
        event = parsed.walk('VEVENT')[0]

        self.assertEqual(event.decoded('DTSTART'), start)
        self.assertEqual(event.decoded('DTEND'), end)
        self.assertEqual(event['DTSTART'].params['VALUE'], 'DATE')
        self.assertEqual(event['DTEND'].params['VALUE'], 'DATE')
        self.assertNotIn('TZID', event['DTSTART'].params)
        self.assertNotIn('TZID', event['DTEND'].params)
        self.assertEqual(parsed.walk('VTIMEZONE'), [])

    def test_make_ical_mixed_date_and_datetime_with_timezone(self) -> None:
        date_start = datetime.date(2026, 9, 22)
        date_end = datetime.date(2026, 9, 23)
        time_start = datetime.datetime(2026, 9, 22, 10, 0)
        time_end = datetime.datetime(2026, 9, 22, 11, 0)
        self.convert.csv_data = [
            ['All day', date_start, date_end, '', ''],
            ['Timed', time_start, time_end, '', ''],
        ]

        calendar = self.convert.make_ical(CSV_CONFIGS)
        parsed = Calendar.from_ical(calendar.to_ical())
        all_day, timed = parsed.walk('VEVENT')

        self.assertEqual(all_day.decoded('DTSTART'), date_start)
        self.assertEqual(all_day.decoded('DTEND'), date_end)
        self.assertEqual(timed['DTSTART'].params['TZID'], 'Europe/Madrid')
        self.assertEqual(timed['DTEND'].params['TZID'], 'Europe/Madrid')
        self.assertEqual(timed.decoded('DTSTART').replace(tzinfo=None), time_start)
        self.assertEqual(timed.decoded('DTEND').replace(tzinfo=None), time_end)
        self.assertEqual(
            timed.decoded('DTSTART').utcoffset(), datetime.timedelta(hours=2),
        )
        self.assertEqual(len(parsed.walk('VTIMEZONE')), 1)

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
