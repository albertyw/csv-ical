"""
This file reads the CSV file and saves an ical file.
There are a bunch of configurable variables
"""

import csv
from icalendar import Calendar, Event


class ConvertCSVToICal():
    def __init__(self):
        self.CSV_FILE_LOCATION = None
        self.SAVE_LOCATION = None
        self.HEADER_COLUMNS_TO_SKIP = 0

        # The variables below refer to the column indexes in the CSV
        self.NAME = 0
        self.START_DATE = 1
        self.END_DATE = 1
        self.DESCRIPTION = 2
        self.LOCATION = 3

        self.csv_data = []
        self.cal = Calendar()

    def read_csv(self):
        """ Read the csv file """
        with open(self.CSV_FILE_LOCATION, 'rb') as csv_file:
            csv_reader = csv.reader(csv_file)
            self.csv_data = list(csv_reader)
        self.csv_data = self.csv_data[self.HEADER_COLUMNS_TO_SKIP:]
        return self.csv_data

    def make_ical(self):
        """ Make iCal entries """
        for row in self.csv_data:
            event = Event()
            event.add('summary', row[self.NAME])
            event.add('dtstart', row[self.START_DATE])
            event.add('dtend', row[self.END_DATE])
            event.add('description', row[self.DESCRIPTION])
            event.add('location', row[self.LOCATION])
            self.cal.add_component(event)
        return self.cal

    def save_ical(self):
        """ Save the calendar instance to a file """
        f = open(self.SAVE_LOCATION, 'wb')
        f.write(self.cal.to_ical())
        f.close()
