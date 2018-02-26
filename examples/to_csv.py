"""
Example conversion of ical to csv
"""

from csv_ical import Convert


convert = Convert()
convert.CSV_FILE_LOCATION = 'examples/BostonCruiseTerminalSchedule.csv'
convert.SAVE_LOCATION = 'examples/arrive.ics'

convert.read_ical(convert.SAVE_LOCATION)
convert.make_csv()
convert.save_csv(convert.CSV_FILE_LOCATION)
