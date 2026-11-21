"""
SelectedPosition stands for the enum 'QStyleOptionHeader::SelectedPosition'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SelectedPosition(CuteNum):
  """
  The enum 'QStyleOptionHeader::SelectedPosition' of Qt, with the 4 names Qt
  gives in it.
  """

  NotAdjacent = Kee[int](0)
  NextIsSelected = Kee[int](1)
  PreviousIsSelected = Kee[int](2)
  NextAndPreviousAreSelected = Kee[int](3)
