"""
Flow stands for the enum 'QListView::Flow' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qlistview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Flow(CuteNum):
  """
  The enum 'QListView::Flow' of Qt, with the 2 names Qt gives in it.
  """

  LeftToRight = Kee[int](0)
  TopToBottom = Kee[int](1)
