Changelog
=========

v2.2.0
------

 - Add a new TIMEZONE configuration
 - Officially support python 3.13
 - Update dependencies


v2.1.2
------

 - Fix examples not running idempotently
 - Update dependencies
 - Fix lint


v2.1.1
------

 - Drop support for python 3.7
 - Add `Config` and `ConfigOverride` types
 - Various cleanup and fixes


v2.1.0
------

 - Allow customizable csv delimiters
 - Packaging updates
 - Update dependencies


v2.0.6
------

 - Switch setup.py to pyproject
 - Update dependencies


v2.0.5
------

 - Add support for python 3.11
 - Dependency updates
 - Updates to python publishing


v2.0.4
------

 - Add full type annotations and add strict mypy typing
 - Switch README to markdown


v2.0.3
------

 - Add support for python 3.10 and drop support for python 3.5 and 3.6 (though it should still work)
 - Switch to Drone CI
 - Clean up testing and examples
 - Update dependencies


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
