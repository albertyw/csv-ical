"""
Example conversion of ical to csv
"""

from csv_ical import Convert


SAVE_LOCATION = 'examples/example.ics'
CSV_FILE_LOCATION = 'examples/example.csv'

csv_delimiter = ','

convert = Convert()
convert.read_ical(SAVE_LOCATION)
convert.make_csv()
convert.save_csv(CSV_FILE_LOCATION, csv_delimiter)
