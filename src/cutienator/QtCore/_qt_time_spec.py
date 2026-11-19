"""
TimeSpec stands for the enum 'Qt::TimeSpec' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TimeSpec(CuteNum):
  """
  The enum 'Qt::TimeSpec' of Qt, with the 4 names Qt gives in it.
  """

  LocalTime = Kee[int](0)
  UTC = Kee[int](1)
  OffsetFromUTC = Kee[int](2)
  TimeZone = Kee[int](3)
