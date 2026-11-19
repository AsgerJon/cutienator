"""
ColorModel stands for the enum 'QPdfWriter::ColorModel' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpdfwriter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ColorModel(CuteNum, scoped=True):
  """
  The enum 'QPdfWriter::ColorModel' of Qt, with the 4 names Qt gives in it.
  C++ keeps these names inside the enum, so the class that holds the enum
  does not have them.
  """

  RGB = Kee[int](0)
  Grayscale = Kee[int](1)
  CMYK = Kee[int](2)
  Auto = Kee[int](3)
