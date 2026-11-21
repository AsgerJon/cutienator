"""
System stands for the enum 'QCalendar::System' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qcalendar.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class System(CuteNum, scoped=True):
  """
  The enum 'QCalendar::System' of Qt, with the 7 names Qt gives in it. C++
  keeps these names inside the enum, so the class that holds the enum does
  not have them.
  """

  Gregorian = Kee[int](0)
  Julian = Kee[int](8)
  Milankovic = Kee[int](9)
  Jalali = Kee[int](10)
  IslamicCivil = Kee[int](11)
  Last = Kee[int](11)
  User = Kee[int](-1)
