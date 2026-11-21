"""
SortIndicator stands for the enum 'QStyleOptionHeader::SortIndicator' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SortIndicator(CuteNum):
  """
  The enum 'QStyleOptionHeader::SortIndicator' of Qt, with the 3 names Qt
  gives in it.
  """

  NULL = Kee[int](0)
  SortUp = Kee[int](1)
  SortDown = Kee[int](2)
