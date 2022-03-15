"""
This file reads the CSV file and saves an ical file.
There are a bunch of configurable variables
"""

import csv
import datetime
from pathlib import Path
from platform import uname
from typing import Any, Dict, List, Optional, Union
from uuid import uuid4

from icalendar import Calendar, Event


DEFAULT_CONFIG = {
    'HEADER_ROWS_TO_SKIP':  0,

    # The variables below refer to the column indexes in the CSV
    'CSV_NAME': 0,
    'CSV_START_DATE': 1,
    'CSV_END_DATE': 1,
    'CSV_DESCRIPTION': 2,
    'CSV_LOCATION': 3,
}


class Convert():
    def __init__(self) -> None:
        self.csv_data: List[List[Any]] = []
        self.cal: Calendar = None

    def _generate_configs_from_default(
        self,
        overrides: Optional[Dict[str, int]] = None,
    ) -> Dict[str, int]:
        """ Generate configs by inheriting from defaults """
        config = DEFAULT_CONFIG.copy()
        if not overrides:
            overrides = {}
        for k, v in overrides.items():
            config[k] = v
        return config

    def read_ical(self, ical_file_location: Union[str, Path]) -> Calendar:
        """ Read the ical file """
        with open(ical_file_location, 'r', encoding='utf-8') as ical_file:
            data = ical_file.read()
        self.cal = Calendar.from_ical(data)
        return self.cal

    def read_csv(
        self,
        csv_location: Union[str, Path],
        csv_configs: Optional[Dict[str, int]] = None
    ) -> List[List[Any]]:
        """ Read the csv file """
        csv_configs = self._generate_configs_from_default(csv_configs)
        with open(csv_location, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            self.csv_data = list(csv_reader)
        self.csv_data = self.csv_data[csv_configs['HEADER_ROWS_TO_SKIP']:]
        return self.csv_data

    def make_ical(
        self,
        csv_configs: Optional[Dict[str, int]] = None,
    ) -> Calendar:
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
            event.add('uid', uuid4().hex + '@' + uname().node)
            event.add('dtstamp', datetime.datetime.now())
            self.cal.add_component(event)
        return self.cal

    def make_csv(self) -> None:
        """ Make CSV """
        for event in self.cal.subcomponents:
            if event.name != 'VEVENT':
                continue
            dtstart = ''
            if event.get('DTSTART'):
                dtstart = event.get('DTSTART').dt
            dtend = ''
            if event.get('DTEND'):
                dtend = event.get('DTEND').dt
            row = [
                event.get('SUMMARY'),
                dtstart,
                dtend,
                event.get('DESCRIPTION'),
                event.get('LOCATION'),
            ]
            row = [str(x) for x in row]
            self.csv_data.append(row)

    def save_ical(self, ical_location: str) -> None:
        """ Save the calendar instance to a file """
        data = self.cal.to_ical()
        with open(ical_location, 'wb') as ical_file:
            ical_file.write(data)

    def save_csv(self, csv_location: str) -> None:
        """ Save the csv to a file """
        with open(csv_location, 'w', encoding='utf-8') as csv_handle:
            writer = csv.writer(csv_handle)
            for row in self.csv_data:
                writer.writerow([r.strip() for r in row])
