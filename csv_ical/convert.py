"""
This file reads the CSV file and saves an ical file.
There are a bunch of configurable variables
"""

import csv
import datetime
from pathlib import Path
from platform import uname
from typing import Any, List, Optional, TypedDict, Union
from uuid import uuid4

from icalendar import Calendar, Event


class Config(TypedDict):
    HEADER_ROWS_TO_SKIP: int
    CSV_NAME: int
    CSV_START_DATE: int
    CSV_END_DATE: int
    CSV_DESCRIPTION: int
    CSV_LOCATION: int
    CSV_DELIMITER: str
class ConfigOverrides(Config, total=False):
    pass
DEFAULT_CONFIG: Config = {
    'HEADER_ROWS_TO_SKIP':  0,

    # The variables below refer to the column indexes in the CSV
    'CSV_NAME': 0,
    'CSV_START_DATE': 1,
    'CSV_END_DATE': 1,
    'CSV_DESCRIPTION': 2,
    'CSV_LOCATION': 3,

    # Delimiter used in CSV file
    'CSV_DELIMITER': ',',
}



class Convert():
    def __init__(self) -> None:
        self.csv_data: List[List[Any]] = []
        self.cal: Calendar = None

    def _generate_configs_from_default(
        self,
        overrides: Optional[ConfigOverrides] = None,
    ) -> Config:
        """ Generate configs by inheriting from defaults """
        config = DEFAULT_CONFIG.copy()
        non_optional_overrides: ConfigOverrides = {}  # type: ignore
        if overrides:
            non_optional_overrides = overrides
        for k, v in non_optional_overrides.items():
            config[k] = v  # type: ignore
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
        csv_configs: Optional[Config] = None,
    ) -> List[List[Any]]:
        """ Read the csv file """
        csv_configs = self._generate_configs_from_default(csv_configs)
        with open(csv_location, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=csv_configs['CSV_DELIMITER'])
            self.csv_data = list(csv_reader)
        self.csv_data = self.csv_data[csv_configs['HEADER_ROWS_TO_SKIP']:]
        return self.csv_data

    def make_ical(
        self,
        csv_configs: Optional[Config] = None,
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

    def save_csv(
        self,
        csv_location: str,
        csv_delimiter: str = ',',
    ) -> None:
        """ Save the csv to a file """
        with open(csv_location, 'w', encoding='utf-8') as csv_handle:
            writer = csv.writer(csv_handle, delimiter=csv_delimiter)
            for row in self.csv_data:
                writer.writerow([r.strip() for r in row])
