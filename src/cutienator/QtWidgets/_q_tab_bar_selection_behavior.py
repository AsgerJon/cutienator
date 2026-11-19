"""
SelectionBehavior stands for the enum 'QTabBar::SelectionBehavior' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qtabbar.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SelectionBehavior(CuteNum):
  """
  The enum 'QTabBar::SelectionBehavior' of Qt, with the 3 names Qt gives in
  it.
  """

  SelectLeftTab = Kee[int](0)
  SelectRightTab = Kee[int](1)
  SelectPreviousTab = Kee[int](2)
