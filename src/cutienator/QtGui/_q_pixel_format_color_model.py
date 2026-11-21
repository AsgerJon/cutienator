"""
ColorModel stands for the enum 'QPixelFormat::ColorModel' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpixelformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ColorModel(CuteNum):
  """
  The enum 'QPixelFormat::ColorModel' of Qt, with the 9 names Qt gives in it.
  """

  RGB = Kee[int](0)
  BGR = Kee[int](1)
  Indexed = Kee[int](2)
  Grayscale = Kee[int](3)
  CMYK = Kee[int](4)
  HSL = Kee[int](5)
  HSV = Kee[int](6)
  YUV = Kee[int](7)
  Alpha = Kee[int](8)
