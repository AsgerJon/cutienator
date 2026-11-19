"""
ButtonSymbols stands for the enum 'QAbstractSpinBox::ButtonSymbols' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qabstractspinbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ButtonSymbols(CuteNum):
  """
  The enum 'QAbstractSpinBox::ButtonSymbols' of Qt, with the 3 names Qt gives
  in it.
  """

  UpDownArrows = Kee[int](0)
  PlusMinus = Kee[int](1)
  NoButtons = Kee[int](2)
