"""
WindowFrameSection stands for the enum 'Qt::WindowFrameSection' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class WindowFrameSection(CuteNum):
  """
  The enum 'Qt::WindowFrameSection' of Qt, with the 10 names Qt gives in it.
  """

  NoSection = Kee[int](0)
  LeftSection = Kee[int](1)
  TopLeftSection = Kee[int](2)
  TopSection = Kee[int](3)
  TopRightSection = Kee[int](4)
  RightSection = Kee[int](5)
  BottomRightSection = Kee[int](6)
  BottomSection = Kee[int](7)
  BottomLeftSection = Kee[int](8)
  TitleBarArea = Kee[int](9)
