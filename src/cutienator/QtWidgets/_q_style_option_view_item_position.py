"""
Position stands for the enum 'QStyleOptionViewItem::Position' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Position(CuteNum):
  """
  The enum 'QStyleOptionViewItem::Position' of Qt, with the 4 names Qt gives
  in it.
  """

  Left = Kee[int](0)
  Right = Kee[int](1)
  Top = Kee[int](2)
  Bottom = Kee[int](3)
