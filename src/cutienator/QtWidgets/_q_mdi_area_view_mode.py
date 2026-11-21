"""
ViewMode stands for the enum 'QMdiArea::ViewMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qmdiarea.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ViewMode(CuteNum):
  """
  The enum 'QMdiArea::ViewMode' of Qt, with the 2 names Qt gives in it.
  """

  SubWindowView = Kee[int](0)
  TabbedView = Kee[int](1)
