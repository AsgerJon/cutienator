"""
The 'cutienator.example' package shows the whole way from a Qt class to
Python once, for eleven of QObject's functions: the ritual files giving them
plain names, the class compiling those into a shared object, and the
calls into it.

  python -m cutienator.example    builds, then calls every function
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ..occult import Build
from ._calls import SIGNATURES, openExample, readText

__all__ = (
    'Build',
    'SIGNATURES',
    'openExample',
    'readText',
)
