"""
GestureType stands for the enum 'Qt::GestureType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class GestureType(CuteNum):
  """
  The enum 'Qt::GestureType' of Qt, with the 7 names Qt gives in it.
  """

  TapGesture = Kee[int](1)
  TapAndHoldGesture = Kee[int](2)
  PanGesture = Kee[int](3)
  PinchGesture = Kee[int](4)
  SwipeGesture = Kee[int](5)
  CustomGesture = Kee[int](256)
  LastGestureType = Kee[int](4294967295)
