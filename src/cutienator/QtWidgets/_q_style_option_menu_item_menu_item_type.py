"""
MenuItemType stands for the enum 'QStyleOptionMenuItem::MenuItemType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MenuItemType(CuteNum):
  """
  The enum 'QStyleOptionMenuItem::MenuItemType' of Qt, with the 8 names Qt
  gives in it.
  """

  Normal = Kee[int](0)
  DefaultItem = Kee[int](1)
  Separator = Kee[int](2)
  SubMenu = Kee[int](3)
  Scroller = Kee[int](4)
  TearOff = Kee[int](5)
  Margin = Kee[int](6)
  EmptyArea = Kee[int](7)
