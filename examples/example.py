"""
This file is an exmaple for running the conversion script
"""

import sys
# Yeah this is a hack
sys.path.append('.')
sys.path.append('../')

from convert import Convert
from datetime import datetime

convert = Convert()
convert.CSV_FILE_LOCATION = 'examples/BostonCruiseTerminalSchedule.csv'
convert.SAVE_LOCATION = 'examples/example.ics'
convert.HEADER_COLUMNS_TO_SKIP = 2
convert.NAME = 3
convert.START_DATE = 2
convert.END_DATE = 2
convert.DESCRIPTION = 6
convert.LOCATION = 9

convert.read_csv()
for row in convert.csv_data:
    row[convert.START_DATE] = datetime.strptime(row[convert.START_DATE], '%m/%d/%y').date()
    
convert.make_ical()
convert.save_ical()
