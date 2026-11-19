"""
DragDropMode stands for the enum 'QAbstractItemView::DragDropMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qabstractitemview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class DragDropMode(CuteNum):
  """
  The enum 'QAbstractItemView::DragDropMode' of Qt, with the 5 names Qt gives
  in it.
  """

  NoDragDrop = Kee[int](0)
  DragOnly = Kee[int](1)
  DropOnly = Kee[int](2)
  DragDrop = Kee[int](3)
  InternalMove = Kee[int](4)
