"""
InsertPolicy stands for the enum 'QComboBox::InsertPolicy' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qcombobox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class InsertPolicy(CuteNum):
  """
  The enum 'QComboBox::InsertPolicy' of Qt, with the 7 names Qt gives in it.
  """

  NoInsert = Kee[int](0)
  InsertAtTop = Kee[int](1)
  InsertAtCurrent = Kee[int](2)
  InsertAtBottom = Kee[int](3)
  InsertAfterCurrent = Kee[int](4)
  InsertBeforeCurrent = Kee[int](5)
  InsertAlphabetically = Kee[int](6)
