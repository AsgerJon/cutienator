"""
ColorSpace stands for the enum 'QSurfaceFormat::ColorSpace' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qsurfaceformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ColorSpace(CuteNum):
  """
  The enum 'QSurfaceFormat::ColorSpace' of Qt, with the 2 names Qt gives in
  it.
  """

  DefaultColorSpace = Kee[int](0)
  sRGBColorSpace = Kee[int](1)
