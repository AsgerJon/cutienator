"""
TabPosition stands for the enum 'QStyleOptionTab::TabPosition' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TabPosition(CuteNum):
  """
  The enum 'QStyleOptionTab::TabPosition' of Qt, with the 5 names Qt gives in
  it.
  """

  Beginning = Kee[int](0)
  Middle = Kee[int](1)
  End = Kee[int](2)
  OnlyOneTab = Kee[int](3)
  Moving = Kee[int](4)
