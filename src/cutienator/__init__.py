"""
The 'cutienator' provides Python bindings to the occult world of C++.

The classes of Qt are in packages named after the parts of Qt, the way
PySide6 has them: 'cutienator.QtCore' so far.

  from cutienator.QtCore import QObject
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

__version__ = '0.0.1-dev1'

from . import cute

__all__ = (
    'cute',
)
