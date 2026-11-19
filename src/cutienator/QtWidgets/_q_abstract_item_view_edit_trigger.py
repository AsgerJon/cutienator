"""
EditTrigger stands for the flags enum 'QAbstractItemView::EditTrigger' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qabstractitemview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class EditTrigger(CuteFlags):
  """
  The flags enum 'QAbstractItemView::EditTrigger' of Qt, with the 7 names Qt
  gives in it. Qt names the type of its combinations
  'QAbstractItemView::EditTriggers'.
  """

  NoEditTriggers = 0x0
  CurrentChanged = 0x1
  DoubleClicked = 0x2
  SelectedClicked = 0x4
  EditKeyPressed = 0x8
  AnyKeyPressed = 0x10
  AllEditTriggers = 0x1f
