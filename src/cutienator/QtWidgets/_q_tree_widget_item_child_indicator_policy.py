"""
ChildIndicatorPolicy stands for the enum
'QTreeWidgetItem::ChildIndicatorPolicy' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qtreewidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ChildIndicatorPolicy(CuteNum):
  """
  The enum 'QTreeWidgetItem::ChildIndicatorPolicy' of Qt, with the 3 names Qt
  gives in it.
  """

  ShowIndicator = Kee[int](0)
  DontShowIndicator = Kee[int](1)
  DontShowIndicatorWhenChildless = Kee[int](2)
