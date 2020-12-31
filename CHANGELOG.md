Changelog
=========

v2.0.2
------

 - Switched to PEP-526 type hints (this removes support for python versions less than 3.5)
 - Add `DTSTAMP` and `uid` fields into output iCal


v2.0.1
------

 - Support parsing events with no `DSTART` or `DTEND` properties
 - Update dependencies


v2.0.0
------

 - Remove python 2 support
 - Simplify code


v1.0.5
------

 - Fix issue with utf-8 encoding and newlines
 - Fix support for python 2
 - Update dependencies


v1.0.4
------

 - Update dependencies
 - Don't allow library to modify global config (@AlbertoMarnetto)


v1.0.3
------

 - Fix getting calendar end time
 - Make converting ical to csv conversion fail gracefully on nonexistent fields
 - Dependency updates


v1.0.2
------

 - Add PEP484 type hints


v1.0.1
------

 - Full test coverage
 - Updated examples
 - Updated dependencies


v1.0.0
------

 - Initial release
