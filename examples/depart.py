"""
This file is an exmaple for running the conversion script
"""

from datetime import datetime, timedelta
import sys

sys.path.append('.')
sys.path.append('../')

from convert import ConvertCSVToICal  # NOQA

convert = ConvertCSVToICal()
csv_file_location = 'examples/BostonCruiseTerminalSchedule.csv'
ical_file_location = 'examples/depart.ics'
config = {
    'HEADER_COLUMNS_TO_SKIP': 2,
    'CSV_NAME': 3,
    'CSV_START_DATE': 7,
    'CSV_END_DATE': 8,
    'CSV_DESCRIPTION': 6,
    'CSV_LOCATION': 9,
}

convert.read_csv(csv_file_location, config)
i = 0
while i < len(convert.csv_data):
    row = convert.csv_data[i]
    start_date = row[2] + '-'+row[config['CSV_END_DATE']]
    try:
        row[config['CSV_START_DATE']] = datetime.strptime(
            start_date,
            '%m/%d/%y-%H:%M'
        )
        row[config['CSV_END_DATE']] = \
            row[config['CSV_START_DATE']]+timedelta(hours=1)
        i += 1
    except ValueError:
        convert.csv_data.pop(i)
    row[config['CSV_NAME']] = 'Depart '+row[config['CSV_NAME']]

convert.make_ical(config)
convert.save_ical(ical_file_location)
