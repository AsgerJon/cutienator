"""
Mode stands for the enum 'QLCDNumber::Mode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qlcdnumber.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Mode(CuteNum):
  """
  The enum 'QLCDNumber::Mode' of Qt, with the 4 names Qt gives in it.
  """

  Hex = Kee[int](0)
  Dec = Kee[int](1)
  Oct = Kee[int](2)
  Bin = Kee[int](3)
