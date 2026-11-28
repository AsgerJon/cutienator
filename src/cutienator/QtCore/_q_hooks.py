"""
QHooks stands for the namespace 'QHooks' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QHooks:
  """
  The namespace 'QHooks' of Qt, which holds no objects. It holds the 1 enums
  Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class HookIndex(CuteNum):
    """
    The enum 'QHooks::HookIndex' of Qt, with the 8 names Qt gives in it.
    """

    HookDataVersion = Kee[int](0)
    HookDataSize = Kee[int](1)
    QtVersion = Kee[int](2)
    AddQObject = Kee[int](3)
    RemoveQObject = Kee[int](4)
    Startup = Kee[int](5)
    TypeInformationVersion = Kee[int](6)
    LastHookIndex = Kee[int](7)
