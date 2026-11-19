"""
SelectionMode stands for the enum 'QAbstractItemView::SelectionMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qabstractitemview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SelectionMode(CuteNum):
  """
  The enum 'QAbstractItemView::SelectionMode' of Qt, with the 5 names Qt
  gives in it.
  """

  NoSelection = Kee[int](0)
  SingleSelection = Kee[int](1)
  MultiSelection = Kee[int](2)
  ExtendedSelection = Kee[int](3)
  ContiguousSelection = Kee[int](4)
