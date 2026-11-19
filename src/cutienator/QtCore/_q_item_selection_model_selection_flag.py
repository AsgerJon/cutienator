"""
SelectionFlag stands for the flags enum 'QItemSelectionModel::SelectionFlag'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qitemselectionmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class SelectionFlag(CuteFlags):
  """
  The flags enum 'QItemSelectionModel::SelectionFlag' of Qt, with the 11
  names Qt gives in it. Qt names the type of its combinations
  'QItemSelectionModel::SelectionFlags'.
  """

  NoUpdate = 0x0
  Clear = 0x1
  Select = 0x2
  Deselect = 0x4
  Toggle = 0x8
  Current = 0x10
  Rows = 0x20
  Columns = 0x40
  SelectCurrent = 0x12
  ToggleCurrent = 0x18
  ClearAndSelect = 0x3
