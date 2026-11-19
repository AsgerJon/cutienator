"""
SelectionBehavior stands for the enum 'QAbstractItemView::SelectionBehavior'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qabstractitemview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SelectionBehavior(CuteNum):
  """
  The enum 'QAbstractItemView::SelectionBehavior' of Qt, with the 3 names Qt
  gives in it.
  """

  SelectItems = Kee[int](0)
  SelectRows = Kee[int](1)
  SelectColumns = Kee[int](2)
