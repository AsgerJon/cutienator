"""
LayoutChangeHint stands for the enum 'QAbstractItemModel::LayoutChangeHint'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class LayoutChangeHint(CuteNum):
  """
  The enum 'QAbstractItemModel::LayoutChangeHint' of Qt, with the 3 names Qt
  gives in it.
  """

  NoLayoutChangeHint = Kee[int](0)
  VerticalSortHint = Kee[int](1)
  HorizontalSortHint = Kee[int](2)
