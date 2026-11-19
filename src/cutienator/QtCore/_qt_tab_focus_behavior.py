"""
TabFocusBehavior stands for the enum 'Qt::TabFocusBehavior' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TabFocusBehavior(CuteNum):
  """
  The enum 'Qt::TabFocusBehavior' of Qt, with the 4 names Qt gives in it.
  """

  NoTabFocus = Kee[int](0)
  TabFocusTextControls = Kee[int](1)
  TabFocusListControls = Kee[int](2)
  TabFocusAllControls = Kee[int](255)
