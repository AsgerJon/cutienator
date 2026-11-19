"""
EndEditHint stands for the enum 'QAbstractItemDelegate::EndEditHint' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qabstractitemdelegate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class EndEditHint(CuteNum):
  """
  The enum 'QAbstractItemDelegate::EndEditHint' of Qt, with the 5 names Qt
  gives in it.
  """

  NoHint = Kee[int](0)
  EditNextItem = Kee[int](1)
  EditPreviousItem = Kee[int](2)
  SubmitModelCache = Kee[int](3)
  RevertModelCache = Kee[int](4)
