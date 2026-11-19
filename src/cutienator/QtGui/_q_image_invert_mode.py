"""
InvertMode stands for the enum 'QImage::InvertMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qimage.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class InvertMode(CuteNum):
  """
  The enum 'QImage::InvertMode' of Qt, with the 2 names Qt gives in it.
  """

  InvertRgb = Kee[int](0)
  InvertRgba = Kee[int](1)
