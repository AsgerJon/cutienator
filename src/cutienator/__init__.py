"""
The 'cutienator' provides Python bindings to the occult world of C++.

The classes of Qt are in packages named after the parts of Qt, the way
PySide6 has them: 'cutienator.QtCore' and 'cutienator.QtWidgets' so far.

  from cutienator.QtCore import QObject
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

__version__ = '0.0.1-dev1'

from ._cpp_addr import CppAddr
from ._cpp_box import CppBox
from ._wait import WAIT
from ._waiting_overload import WaitingOverload
from ._cute_overload import CuteOverload
from ._cute_load_hook import CuteLoadHook
from ._cute_space import CuteSpace
from ._meta_cute import MetaCute
from ._cute_mixin import CuteMixin
from ._ugly import Ugly

__all__ = (
    'CppAddr',
    'CppBox',
    'WAIT',
    'WaitingOverload',
    'CuteOverload',
    'CuteLoadHook',
    'CuteSpace',
    'MetaCute',
    'CuteMixin',
    'Ugly',
)
