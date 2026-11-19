"""
TickPosition stands for the enum 'QSlider::TickPosition' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qslider.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TickPosition(CuteNum):
  """
  The enum 'QSlider::TickPosition' of Qt, with the 6 names Qt gives in it.
  """

  NoTicks = Kee[int](0)
  TicksAbove = Kee[int](1)
  TicksLeft = Kee[int](1)
  TicksBelow = Kee[int](2)
  TicksRight = Kee[int](2)
  TicksBothSides = Kee[int](3)
