"""
Corner stands for the enum 'Qt::Corner' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Corner(CuteNum):
  """
  The enum 'Qt::Corner' of Qt, with the 4 names Qt gives in it.
  """

  TopLeftCorner = Kee[int](0)
  TopRightCorner = Kee[int](1)
  BottomLeftCorner = Kee[int](2)
  BottomRightCorner = Kee[int](3)
