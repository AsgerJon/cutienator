"""
State stands for the enum 'QScroller::State' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qscroller.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class State(CuteNum):
  """
  The enum 'QScroller::State' of Qt, with the 4 names Qt gives in it.
  """

  Inactive = Kee[int](0)
  Pressed = Kee[int](1)
  Dragging = Kee[int](2)
  Scrolling = Kee[int](3)
