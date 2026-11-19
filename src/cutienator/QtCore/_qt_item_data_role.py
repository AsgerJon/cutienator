"""
ItemDataRole stands for the enum 'Qt::ItemDataRole' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ItemDataRole(CuteNum):
  """
  The enum 'Qt::ItemDataRole' of Qt, with the 26 names Qt gives in it.
  """

  DisplayRole = Kee[int](0)
  DecorationRole = Kee[int](1)
  EditRole = Kee[int](2)
  ToolTipRole = Kee[int](3)
  StatusTipRole = Kee[int](4)
  WhatsThisRole = Kee[int](5)
  FontRole = Kee[int](6)
  TextAlignmentRole = Kee[int](7)
  BackgroundRole = Kee[int](8)
  ForegroundRole = Kee[int](9)
  CheckStateRole = Kee[int](10)
  AccessibleTextRole = Kee[int](11)
  AccessibleDescriptionRole = Kee[int](12)
  SizeHintRole = Kee[int](13)
  InitialSortOrderRole = Kee[int](14)
  DisplayPropertyRole = Kee[int](27)
  DecorationPropertyRole = Kee[int](28)
  ToolTipPropertyRole = Kee[int](29)
  StatusTipPropertyRole = Kee[int](30)
  WhatsThisPropertyRole = Kee[int](31)
  RangeModelDataRole = Kee[int](40)
  RangeModelAdapterRole = Kee[int](41)
  UserRole = Kee[int](256)
  StandardItemFlagsRole = Kee[int](255)
  FileInfoRole = Kee[int](252)
  RemoteObjectsCacheRole = Kee[int](255)
