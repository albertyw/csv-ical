"""
This file reads the CSV file and saves an ical file.  
There are a bunch of configurable variables
"""

import csv
from icalendar import Calendar, Event
from datetime import datetime, date

CSV_FILE_LOCATION = 'examples/BostonCruiseTerminalSchedule.csv'
SAVE_LOCATION = 'example.ics'
HEADER_COLUMNS_TO_SKIP = 2

# The variables below refer to the column indexes in the CSV
NAME = 3
DATE = 2
DESCRIPTION = 6
LOCATION = 9

# Read the csv file
#
def read_csv():
    csv_reader = csv.reader(open(CSV_FILE_LOCATION, 'rb'))
    i = 0
    csv_data = []
    for row in csv_reader:
        if i < HEADER_COLUMNS_TO_SKIP:
            i += 1
            continue
        csv_data.append(row)
    return csv_data
    

# Make iCal entries
#
def make_ical(csv_data):
    cal = Calendar()
    for row in csv_data:
        event = Event()
        event.add('summary', row[NAME])
        event.add('dtstart', row[DATE])
        event.add('dtend', row[DATE])
        event.add('description', row[DESCRIPTION])
        event.add('location', row[LOCATION])
        cal.add_component(event)
    return cal
    
# Save the calendar instance to a file
#
def save_ical(cal):
    f = open(SAVE_LOCATION, 'wb')
    f.write(cal.to_ical())
    f.close()
    
    
csv_data = read_csv()
for row in csv_data:
    row[DATE] = datetime.strptime(row[DATE], '%m/%d/%y').date()
cal = make_ical(csv_data)
save_ical(cal)
