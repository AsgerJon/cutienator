"""
AlphaPosition stands for the enum 'QPixelFormat::AlphaPosition' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpixelformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class AlphaPosition(CuteNum):
  """
  The enum 'QPixelFormat::AlphaPosition' of Qt, with the 2 names Qt gives in
  it.
  """

  AtBeginning = Kee[int](0)
  AtEnd = Kee[int](1)
