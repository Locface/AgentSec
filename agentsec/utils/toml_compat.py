"""TOML compatibility layer for Python 3.10+.

Python 3.11 introduced ``tomllib`` as a stdlib module.
On Python 3.10, the third-party ``tomli`` package provides the same API.

Usage::

    from agentsec.utils.toml_compat import tomllib, TOMLDecodeError

``tomllib`` and ``TOMLDecodeError`` are drop-in compatible with the
stdlib module (PEP 680).
"""

import sys

__all__ = ["tomllib", "TOMLDecodeError"]

if sys.version_info >= (3, 11):
    import tomllib as _tomllib

    tomllib = _tomllib
    TOMLDecodeError = _tomllib.TOMLDecodeError
else:
    import tomli as _tomli

    tomllib = _tomli
    TOMLDecodeError = _tomli.TOMLDecodeError
