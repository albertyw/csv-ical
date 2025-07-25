# CSV/iCal Converter

[![PyPI](https://img.shields.io/pypi/v/csv-ical)](https://pypi.org/project/csv-ical/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/csv-ical)
![PyPI - License](https://img.shields.io/pypi/l/csv-ical)

[![Build Status](https://drone.albertyw.com/api/badges/albertyw/csv-ical/status.svg)](https://drone.albertyw.com/albertyw/csv-ical)
[![Maintainability](https://qlty.sh/gh/albertyw/projects/csv-ical/maintainability.svg)](https://qlty.sh/gh/albertyw/projects/csv-ical)
[![Code Coverage](https://qlty.sh/gh/albertyw/projects/csv-ical/coverage.svg)](https://qlty.sh/gh/albertyw/projects/csv-ical)

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
pip install -e .[test]
ruff check .
mypy . --strict --ignore-missing-imports
coverage run -m unittest
coverage report -m
```
