"""
Spec stands for the enum 'QColor::Spec' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qcolor.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Spec(CuteNum):
  """
  The enum 'QColor::Spec' of Qt, with the 6 names Qt gives in it.
  """

  Invalid = Kee[int](0)
  Rgb = Kee[int](1)
  Hsv = Kee[int](2)
  Cmyk = Kee[int](3)
  Hsl = Kee[int](4)
  ExtendedRgb = Kee[int](5)
