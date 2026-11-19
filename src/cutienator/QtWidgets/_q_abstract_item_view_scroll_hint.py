"""
ScrollHint stands for the enum 'QAbstractItemView::ScrollHint' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qabstractitemview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ScrollHint(CuteNum):
  """
  The enum 'QAbstractItemView::ScrollHint' of Qt, with the 4 names Qt gives
  in it.
  """

  EnsureVisible = Kee[int](0)
  PositionAtTop = Kee[int](1)
  PositionAtBottom = Kee[int](2)
  PositionAtCenter = Kee[int](3)
