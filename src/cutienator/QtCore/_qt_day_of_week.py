"""
DayOfWeek stands for the enum 'Qt::DayOfWeek' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class DayOfWeek(CuteNum):
  """
  The enum 'Qt::DayOfWeek' of Qt, with the 7 names Qt gives in it.
  """

  Monday = Kee[int](1)
  Tuesday = Kee[int](2)
  Wednesday = Kee[int](3)
  Thursday = Kee[int](4)
  Friday = Kee[int](5)
  Saturday = Kee[int](6)
  Sunday = Kee[int](7)
