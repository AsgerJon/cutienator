"""
TabShape stands for the enum 'QTabWidget::TabShape' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qtabwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TabShape(CuteNum):
  """
  The enum 'QTabWidget::TabShape' of Qt, with the 2 names Qt gives in it.
  """

  Rounded = Kee[int](0)
  Triangular = Kee[int](1)
