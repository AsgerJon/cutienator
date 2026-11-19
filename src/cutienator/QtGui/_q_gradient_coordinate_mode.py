"""
CoordinateMode stands for the enum 'QGradient::CoordinateMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qbrush.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class CoordinateMode(CuteNum):
  """
  The enum 'QGradient::CoordinateMode' of Qt, with the 4 names Qt gives in
  it.
  """

  LogicalMode = Kee[int](0)
  StretchToDeviceMode = Kee[int](1)
  ObjectBoundingMode = Kee[int](2)
  ObjectMode = Kee[int](3)
