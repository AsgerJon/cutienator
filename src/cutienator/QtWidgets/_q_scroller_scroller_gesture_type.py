"""
ScrollerGestureType stands for the enum 'QScroller::ScrollerGestureType' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qscroller.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ScrollerGestureType(CuteNum):
  """
  The enum 'QScroller::ScrollerGestureType' of Qt, with the 4 names Qt gives
  in it.
  """

  TouchGesture = Kee[int](0)
  LeftMouseButtonGesture = Kee[int](1)
  RightMouseButtonGesture = Kee[int](2)
  MiddleMouseButtonGesture = Kee[int](3)
