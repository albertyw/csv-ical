"""
This file is an exmaple for running the conversion script
"""

from datetime import datetime, timedelta
import sys

sys.path.append('.')
sys.path.append('../')

from convert import ConvertCSVToICal  # NOQA

convert = ConvertCSVToICal()
convert.CSV_FILE_LOCATION = 'examples/BostonCruiseTerminalSchedule.csv'
convert.SAVE_LOCATION = 'examples/arrive.ics'
convert.HEADER_COLUMNS_TO_SKIP = 2
convert.NAME = 3
convert.START_DATE = 7
convert.END_DATE = 8
convert.DESCRIPTION = 6
convert.LOCATION = 9

convert.read_csv()
i = 0
while i < len(convert.csv_data):
    row = convert.csv_data[i]
    start_date = row[2] + '-'+row[convert.START_DATE]
    try:
        row[convert.START_DATE] = datetime.strptime(
            start_date, '%m/%d/%y-%H:%M'
        )
        row[convert.END_DATE] = row[convert.START_DATE]+timedelta(hours=1)
        i += 1
    except ValueError:
        convert.csv_data.pop(i)
    row[convert.NAME] = 'Arrive '+row[convert.NAME]

convert.make_ical()
convert.save_ical()
