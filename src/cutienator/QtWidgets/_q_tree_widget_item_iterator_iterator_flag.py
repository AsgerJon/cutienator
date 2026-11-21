"""
IteratorFlag stands for the flags enum
'QTreeWidgetItemIterator::IteratorFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qtreewidgetitemiterator.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from ..cute import CuteFlags


class IteratorFlag(CuteFlags):
  """
  The flags enum 'QTreeWidgetItemIterator::IteratorFlag' of Qt, with the 20
  names Qt gives in it. Qt names the type of its combinations
  'QTreeWidgetItemIterator::IteratorFlags'.
  """

  All = 0x0
  Hidden = 0x1
  NotHidden = 0x2
  Selected = 0x4
  Unselected = 0x8
  Selectable = 0x10
  NotSelectable = 0x20
  DragEnabled = 0x40
  DragDisabled = 0x80
  DropEnabled = 0x100
  DropDisabled = 0x200
  HasChildren = 0x400
  NoChildren = 0x800
  Checked = 0x1000
  NotChecked = 0x2000
  Enabled = 0x4000
  Disabled = 0x8000
  Editable = 0x10000
  NotEditable = 0x20000
  UserFlag = 0x1000000
