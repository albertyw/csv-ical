"""
This file reads the CSV file and saves an ical file.
There are a bunch of configurable variables
"""

import csv
from icalendar import Calendar, Event

DEFAULT_CONFIG = {
    'HEADER_COLUMNS_TO_SKIP':  0,

    # The variables below refer to the column indexes in the CSV
    'CSV_NAME': 0,
    'CSV_START_DATE': 1,
    'CSV_END_DATE': 1,
    'CSV_DESCRIPTION': 2,
    'CSV_LOCATION': 3,
}


class Convert():
    def __init__(self):
        self.csv_data = []
        self.cal = None

    def _generate_configs_from_default(self, overrides=None):
        """ Generate configs by inheriting from defaults """
        config = DEFAULT_CONFIG
        if not overrides:
            overrides = {}
        for k, v in overrides.items():
            config[k] = v
        return config

    def read_csv(self, csv_location, csv_configs=None):
        """ Read the csv file """
        csv_configs = self._generate_configs_from_default(csv_configs)
        with open(csv_location, 'rb') as csv_file:
            csv_reader = csv.reader(csv_file)
            self.csv_data = list(csv_reader)
        self.csv_data = self.csv_data[csv_configs['HEADER_COLUMNS_TO_SKIP']:]
        return self.csv_data

    def make_ical(self, csv_configs=None):
        """ Make iCal entries """
        csv_configs = self._generate_configs_from_default(csv_configs)
        self.cal = Calendar()
        for row in self.csv_data:
            event = Event()
            event.add('summary', row[csv_configs['CSV_NAME']])
            event.add('dtstart', row[csv_configs['CSV_START_DATE']])
            event.add('dtend', row[csv_configs['CSV_END_DATE']])
            event.add('description', row[csv_configs['CSV_DESCRIPTION']])
            event.add('location', row[csv_configs['CSV_LOCATION']])
            self.cal.add_component(event)
        return self.cal

    def save_ical(self, ical_location):
        """ Save the calendar instance to a file """
        with open(ical_location, 'wb') as ical_file:
            ical_file.write(self.cal.to_ical())
