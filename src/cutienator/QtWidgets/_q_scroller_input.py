"""
Input stands for the enum 'QScroller::Input' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qscroller.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Input(CuteNum):
  """
  The enum 'QScroller::Input' of Qt, with the 3 names Qt gives in it.
  """

  InputPress = Kee[int](1)
  InputMove = Kee[int](2)
  InputRelease = Kee[int](3)
