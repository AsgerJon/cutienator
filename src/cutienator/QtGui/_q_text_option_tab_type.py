"""
TabType stands for the enum 'QTextOption::TabType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TabType(CuteNum):
  """
  The enum 'QTextOption::TabType' of Qt, with the 4 names Qt gives in it.
  """

  LeftTab = Kee[int](0)
  RightTab = Kee[int](1)
  CenterTab = Kee[int](2)
  DelimiterTab = Kee[int](3)
