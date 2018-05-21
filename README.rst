CSV/iCal Converter
==================

|PyPI| |Python Versions|

|Codeship Status for albertyw/csv-ical| |Dependency Status| |Code Climate| |Test Coverage|


A simple script to convert data in CSV format to iCal format and vice versa.

Installation
------------

.. code:: bash

    pip install csv-ical

Usage
-----

See the example files.

Development
-----------

.. code:: bash

    pip install -r requirements-test.txt
    pip install -r requirements-test-python3.txt
    mypy csv_ical/convert.py --ignore-missing-imports
    coverage run setup.py test
    coverage report -m
    flake8

Publishing
----------

.. code:: bash

    pip install twine
    python setup.py sdist bdist_wheel
    twine upload dist/*

.. |PyPI| image:: https://img.shields.io/pypi/v/csv-ical.svg
   :target: https://pypi.python.org/pypi/csv-ical/
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/csv-ical.svg
   :target: https://github.com/albertyw/csv-ical
.. |Codeship Status for albertyw/csv-ical| image:: https://app.codeship.com/projects/2c87dbd0-f84c-0135-ce47-1a2a752165ba/status?branch=master
   :target: https://app.codeship.com/projects/278164
.. |Dependency Status| image:: https://pyup.io/repos/github/albertyw/csv-ical/shield.svg
   :target: https://pyup.io/repos/github/albertyw/csv-ical/
.. |Code Climate| image:: https://codeclimate.com/github/albertyw/csv-ical/badges/gpa.svg
   :target: https://codeclimate.com/github/albertyw/csv-ical
.. |Test Coverage| image:: https://codeclimate.com/github/albertyw/csv-ical/badges/coverage.svg
   :target: https://codeclimate.com/github/albertyw/csv-ical/coverage
