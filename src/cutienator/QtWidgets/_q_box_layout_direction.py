"""
Direction stands for the enum 'QBoxLayout::Direction' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qboxlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Direction(CuteNum):
  """
  The enum 'QBoxLayout::Direction' of Qt, with the 6 names Qt gives in it.
  """

  LeftToRight = Kee[int](0)
  RightToLeft = Kee[int](1)
  TopToBottom = Kee[int](2)
  BottomToTop = Kee[int](3)
  Down = Kee[int](2)
  Up = Kee[int](3)
