"""
Example conversion of ical to csv
"""

from csv_ical import Convert


SAVE_LOCATION = 'examples/arrive.ics'
CSV_FILE_LOCATION = 'examples/BostonCruiseTerminalSchedule.csv'


convert = Convert()
convert.read_ical(SAVE_LOCATION)
convert.make_csv()
convert.save_csv(CSV_FILE_LOCATION)
