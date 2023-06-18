# CSV/iCal Converter

[![PyPI](https://img.shields.io/pypi/v/csv-ical)](https://pypi.org/project/csv-ical/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/csv-ical)
![PyPI - License](https://img.shields.io/pypi/l/csv-ical)

[![Build Status](https://drone.albertyw.com/api/badges/albertyw/csv-ical/status.svg)](https://drone.albertyw.com/albertyw/csv-ical)
[![Dependency Status](https://pyup.io/repos/github/albertyw/csv-ical/shield.svg)](https://pyup.io/repos/github/albertyw/csv-ical/)
[![Code Climate](https://codeclimate.com/github/albertyw/csv-ical/badges/gpa.svg)](https://codeclimate.com/github/albertyw/csv-ical)
[![Test Coverage](https://codeclimate.com/github/albertyw/csv-ical/badges/coverage.svg)](https://codeclimate.com/github/albertyw/csv-ical/coverage)

A simple script to convert data in CSV format to iCal format and vice
versa.

## Installation

```bash
pip install csv-ical
```

## Usage

See the example files.

## Development

```bash
pip install -r requirements-test.txt
ruff check .
mypy . --strict --ignore-missing-imports
coverage run -m unittest
coverage report -m
```
