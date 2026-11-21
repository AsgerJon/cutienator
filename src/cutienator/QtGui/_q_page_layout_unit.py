"""
Unit stands for the enum 'QPageLayout::Unit' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpagelayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Unit(CuteNum):
  """
  The enum 'QPageLayout::Unit' of Qt, with the 6 names Qt gives in it.
  """

  Millimeter = Kee[int](0)
  Point = Kee[int](1)
  Inch = Kee[int](2)
  Pica = Kee[int](3)
  Didot = Kee[int](4)
  Cicero = Kee[int](5)
