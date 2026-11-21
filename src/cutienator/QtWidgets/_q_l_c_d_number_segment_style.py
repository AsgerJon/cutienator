"""
SegmentStyle stands for the enum 'QLCDNumber::SegmentStyle' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qlcdnumber.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SegmentStyle(CuteNum):
  """
  The enum 'QLCDNumber::SegmentStyle' of Qt, with the 3 names Qt gives in it.
  """

  Outline = Kee[int](0)
  Filled = Kee[int](1)
  Flat = Kee[int](2)
