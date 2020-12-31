#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages
from typing import Dict


# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

about: Dict[str, str] = {}
with open(path.join(here, 'csv_ical', '__version__.py')) as f:
    exec(f.read(), about)

setup(
    name='csv-ical',

    version=about['__version__'],

    description='Convert between CSV and iCal',
    long_description=long_description,

    url='https://github.com/albertyw/csv-ical',

    author='Albert Wang',
    author_email='git@albertyw.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

        'Typing :: Typed',
    ],

    keywords='',

    package_data={"csv_ical": ["py.typed"]},
    packages=find_packages(exclude=["tests"]),

    python_requires='>=3.5',
    install_requires=[
        'icalendar>=4.0.1,<5.0.0',
    ],
    tests_require=[
        'syspath>=1.0.0,<2.0.0',
    ],

    test_suite="csv_ical.tests",

    # testing requires flake8 and coverage but they're listed separately
    # because they need to wrap setup.py
    extras_require={
        'dev': [],
        'test': [],
    },
)
