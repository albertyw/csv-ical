"""
This file reads the CSV file and saves an ical file.  
There are a bunch of configurable variables
"""
import csv
from icalendar import Calendar, Event
from datetime import datetime, date
import pytz

CSV_FILE_LOCATION = 'examples/BostonCruiseTerminalSchedule.csv'
HEADER_COLUMNS_TO_SKIP = 2

# The variables below refer to the column indexes in the CSV
NAME = 3
DATE = 2
DESCRIPTION = 6
LOCATION = 9

# Read the csv file
csv_reader = csv.reader(open(CSV_FILE_LOCATION, 'rb'))
i = 0
csv = []
for row in csv_reader:
    if i < HEADER_COLUMNS_TO_SKIP:
        i += 1
        continue
    csv.append(row)
    
for row in csv:
    row[DATE] = datetime.strptime(row[DATE], '%m/%d/%y').date()
    
# Make iCal entries
cal = Calendar()
for row in csv:
    event = Event()
    event.add('summary', row[NAME])
    event.add('dtstart', row[DATE])
    event.add('dtend', row[DATE])
    event.add('description', row[DESCRIPTION])
    event.add('location', row[LOCATION])
    cal.add_component(event)
    
f = open('example.ics', 'wb')
f.write(cal.to_ical())
f.close()
