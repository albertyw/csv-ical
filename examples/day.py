"""
This file is an exmaple for running the conversion script
"""

from datetime import datetime
import sys

sys.path.append('.')
sys.path.append('../')

from convert import ConvertCSVToICal  # NOQA

convert = ConvertCSVToICal()
csv_file_location = 'examples/BostonCruiseTerminalSchedule.csv'
ical_save_location = 'examples/day.ics'
config = {
    'HEADER_COLUMNS_TO_SKIP': 2,
    'CSV_NAME': 3,
    'CSV_START_DATE': 2,
    'CSV_END_DATE': 2,
    'CSV_DESCRIPTION': 6,
    'CSV_LOCATION': 9,
}

convert.read_csv(csv_file_location, config)
for row in convert.csv_data:
    row[config['CSV_START_DATE']] = datetime.strptime(
        row[config['CSV_START_DATE']],
        '%m/%d/%y'
    ).date()

convert.make_ical(config)
convert.save_ical(ical_save_location)
