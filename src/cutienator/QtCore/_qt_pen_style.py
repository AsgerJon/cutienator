"""
PenStyle stands for the enum 'Qt::PenStyle' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class PenStyle(CuteNum):
  """
  The enum 'Qt::PenStyle' of Qt, with the 8 names Qt gives in it.
  """

  NoPen = Kee[int](0)
  SolidLine = Kee[int](1)
  DashLine = Kee[int](2)
  DotLine = Kee[int](3)
  DashDotLine = Kee[int](4)
  DashDotDotLine = Kee[int](5)
  CustomDashLine = Kee[int](6)
  MPenStyle = Kee[int](15)
