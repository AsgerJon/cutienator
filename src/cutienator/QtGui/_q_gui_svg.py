"""
QGuiSvg stands for the namespace 'QGuiSvg' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QGuiSvg:
  """
  The namespace 'QGuiSvg' of Qt, which holds no objects. It holds the 1 enums
  Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class LengthType(CuteNum):
    """
    The enum 'QGuiSvg::LengthType' of Qt, with the 8 names Qt gives in it.
    """

    LT_PERCENT = Kee[int](0)
    LT_PX = Kee[int](1)
    LT_PC = Kee[int](2)
    LT_PT = Kee[int](3)
    LT_MM = Kee[int](4)
    LT_CM = Kee[int](5)
    LT_IN = Kee[int](6)
    LT_OTHER = Kee[int](7)
