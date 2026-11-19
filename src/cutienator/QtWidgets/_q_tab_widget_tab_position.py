"""
TabPosition stands for the enum 'QTabWidget::TabPosition' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qtabwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TabPosition(CuteNum):
  """
  The enum 'QTabWidget::TabPosition' of Qt, with the 4 names Qt gives in it.
  """

  North = Kee[int](0)
  South = Kee[int](1)
  West = Kee[int](2)
  East = Kee[int](3)
