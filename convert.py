"""
This file reads the CSV file and saves an ical file.  
There are a bunch of configurable variables
"""

import csv
from icalendar import Calendar, Event

class Convert():
    # Initialize some configs
    def __init__(self):
        self.CSV_FILE_LOCATION = None
        self.SAVE_LOCATION = None
        self.HEADER_COLUMNS_TO_SKIP = 0
        
        # The variables below refer to the column indexes in the CSV
        self.NAME = 0
        self.DATE = 1
        self.DESCRIPTION = 2
        self.LOCATION = 3
        
        self.csv_data = []
        self.cal = Calendar()
        
    # Read the csv file
    #
    def read_csv(self):
        csv_reader = csv.reader(open(self.CSV_FILE_LOCATION, 'rb'))
        i = 0
        for row in csv_reader:
            if i < self.HEADER_COLUMNS_TO_SKIP:
                i += 1
                continue
            self.csv_data.append(row)
        return self.csv_data
        
    # Make iCal entries
    #
    def make_ical(self):
        for row in self.csv_data:
            event = Event()
            event.add('summary', row[self.NAME])
            event.add('dtstart', row[self.DATE])
            event.add('dtend', row[self.DATE])
            event.add('description', row[self.DESCRIPTION])
            event.add('location', row[self.LOCATION])
            self.cal.add_component(event)
        return self.cal
        
    # Save the calendar instance to a file
    #
    def save_ical(self):
        f = open(self.SAVE_LOCATION, 'wb')
        f.write(self.cal.to_ical())
        f.close()
        
