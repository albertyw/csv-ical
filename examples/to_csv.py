"""
This file is an exmaple for running the conversion script
"""

from datetime import datetime, timedelta
import sys

sys.path.append('.')
sys.path.append('../')

from convert import Convert  # NOQA

convert = Convert()
convert.CSV_FILE_LOCATION = 'examples/BostonCruiseTerminalSchedule.csv'
convert.SAVE_LOCATION = 'examples/arrive.ics'

convert.read_ical(convert.SAVE_LOCATION)
convert.make_csv()
convert.save_csv(convert.CSV_FILE_LOCATION)
