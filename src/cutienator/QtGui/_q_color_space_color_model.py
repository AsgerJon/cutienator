"""
ColorModel stands for the enum 'QColorSpace::ColorModel' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qcolorspace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ColorModel(CuteNum, scoped=True):
  """
  The enum 'QColorSpace::ColorModel' of Qt, with the 4 names Qt gives in it.
  C++ keeps these names inside the enum, so the class that holds the enum
  does not have them.
  """

  Undefined = Kee[int](0)
  Rgb = Kee[int](1)
  Gray = Kee[int](2)
  Cmyk = Kee[int](3)
