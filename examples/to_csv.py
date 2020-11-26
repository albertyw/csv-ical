"""
Example conversion of ical to csv
"""

from csv_ical import Convert
import sys


convert = Convert()
convert.CSV_FILE_LOCATION = sys.argv[2]
convert.SAVE_LOCATION = sys.argv[1]

convert.read_ical(convert.SAVE_LOCATION)
convert.make_csv()
convert.save_csv(convert.CSV_FILE_LOCATION)
