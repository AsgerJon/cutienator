"""
GlobalColor stands for the enum 'Qt::GlobalColor' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class GlobalColor(CuteNum):
  """
  The enum 'Qt::GlobalColor' of Qt, with the 20 names Qt gives in it.
  """

  color0 = Kee[int](0)
  color1 = Kee[int](1)
  black = Kee[int](2)
  white = Kee[int](3)
  darkGray = Kee[int](4)
  gray = Kee[int](5)
  lightGray = Kee[int](6)
  red = Kee[int](7)
  green = Kee[int](8)
  blue = Kee[int](9)
  cyan = Kee[int](10)
  magenta = Kee[int](11)
  yellow = Kee[int](12)
  darkRed = Kee[int](13)
  darkGreen = Kee[int](14)
  darkBlue = Kee[int](15)
  darkCyan = Kee[int](16)
  darkMagenta = Kee[int](17)
  darkYellow = Kee[int](18)
  transparent = Kee[int](19)
