from convert import Convert
from datetime import datetime

convert = Convert()
convert.CSV_FILE_LOCATION = 'examples/BostonCruiseTerminalSchedule.csv'
convert.SAVE_LOCATION = 'example.ics'
convert.HEADER_COLUMNS_TO_SKIP = 2
convert.NAME = 3
convert.DATE = 2
convert.DESCRIPTION = 6
convert.LOCATION = 9

convert.read_csv()
for row in convert.csv_data:
    row[convert.DATE] = datetime.strptime(row[convert.DATE], '%m/%d/%y').date()
convert.make_ical()
convert.save_ical()
