"""
HighDpiScaleFactorRoundingPolicy stands for the enum
'Qt::HighDpiScaleFactorRoundingPolicy' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class HighDpiScaleFactorRoundingPolicy(CuteNum, scoped=True):
  """
  The enum 'Qt::HighDpiScaleFactorRoundingPolicy' of Qt, with the 6 names Qt
  gives in it. C++ keeps these names inside the enum, so the class that holds
  the enum does not have them.
  """

  Unset = Kee[int](0)
  Round = Kee[int](1)
  Ceil = Kee[int](2)
  Floor = Kee[int](3)
  RoundPreferFloor = Kee[int](4)
  PassThrough = Kee[int](5)
