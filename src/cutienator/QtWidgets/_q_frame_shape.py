"""
Shape stands for the enum 'QFrame::Shape' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qframe.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Shape(CuteNum):
  """
  The enum 'QFrame::Shape' of Qt, with the 7 names Qt gives in it.
  """

  NoFrame = Kee[int](0)
  Box = Kee[int](1)
  Panel = Kee[int](2)
  WinPanel = Kee[int](3)
  HLine = Kee[int](4)
  VLine = Kee[int](5)
  StyledPanel = Kee[int](6)
