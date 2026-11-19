"""
ItemFlag stands for the flags enum 'Qt::ItemFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ItemFlag(CuteFlags):
  """
  The flags enum 'Qt::ItemFlag' of Qt, with the 10 names Qt gives in it. Qt
  names the type of its combinations 'Qt::ItemFlags'.
  """

  NoItemFlags = 0x0
  ItemIsSelectable = 0x1
  ItemIsEditable = 0x2
  ItemIsDragEnabled = 0x4
  ItemIsDropEnabled = 0x8
  ItemIsUserCheckable = 0x10
  ItemIsEnabled = 0x20
  ItemIsAutoTristate = 0x40
  ItemNeverHasChildren = 0x80
  ItemIsUserTristate = 0x100
