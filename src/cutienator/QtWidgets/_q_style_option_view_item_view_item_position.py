"""
ViewItemPosition stands for the enum 'QStyleOptionViewItem::ViewItemPosition'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ViewItemPosition(CuteNum):
  """
  The enum 'QStyleOptionViewItem::ViewItemPosition' of Qt, with the 5 names
  Qt gives in it.
  """

  Invalid = Kee[int](0)
  Beginning = Kee[int](1)
  Middle = Kee[int](2)
  End = Kee[int](3)
  OnlyOne = Kee[int](4)
