Changelog
=========

v2.2.1 (2026-11-22)
-------------------

 - Preserve all-day dates with a configured timezone (from @bensynapse)
 - Officially support python 3.15
 - Update dependencies
 - Publish PyPI packages using OIDC
 - PyPI package metadata updates
 - CI cleanup


v2.2.0 (2025-09-30)
-------------------

 - Add a new TIMEZONE configuration
 - Officially support python 3.13
 - Update dependencies


v2.1.2 (2024-12-09)
-------------------

 - Fix examples not running idempotently
 - Update dependencies
 - Fix lint


v2.1.1 (2024-03-03)
-------------------

 - Drop support for python 3.7
 - Add `Config` and `ConfigOverride` types
 - Various cleanup and fixes


v2.1.0 (2024-03-02)
-------------------

 - Allow customizable csv delimiters
 - Packaging updates
 - Update dependencies


v2.0.6 (2023-10-17)
-------------------

 - Switch setup.py to pyproject
 - Update dependencies


v2.0.5 (2023-06-17)
-------------------

 - Add support for python 3.11
 - Dependency updates
 - Updates to python publishing


v2.0.4 (2022-03-17)
-------------------

 - Add full type annotations and add strict mypy typing
 - Switch README to markdown


v2.0.3 (2022-03-14)
-------------------

 - Add support for python 3.10 and drop support for python 3.5 and 3.6 (though it should still work)
 - Switch to Drone CI
 - Clean up testing and examples
 - Update dependencies


v2.0.2 (2020-12-30)
-------------------

 - Switched to PEP-526 type hints (this removes support for python versions less than 3.5)
 - Add `DTSTAMP` and `uid` fields into output iCal


v2.0.1 (2020-12-26)
-------------------

 - Support parsing events with no `DSTART` or `DTEND` properties
 - Update dependencies


v2.0.0 (2019-08-24)
-------------------

 - Remove python 2 support
 - Simplify code


v1.0.5 (2019-08-23)
-------------------

 - Fix issue with utf-8 encoding and newlines
 - Fix support for python 2
 - Update dependencies


v1.0.4 (2019-04-09)
-------------------

 - Update dependencies
 - Don't allow library to modify global config (@AlbertoMarnetto)


v1.0.3 (2018-10-24)
-------------------

 - Fix getting calendar end time
 - Make converting ical to csv conversion fail gracefully on nonexistent fields
 - Dependency updates


v1.0.2 (2018-04-08)
-------------------

 - Add PEP484 type hints


v1.0.1 (2018-04-08)
-------------------

 - Full test coverage
 - Updated examples
 - Updated dependencies


v1.0.0 (2018-02-25)
-------------------

 - Initial release
