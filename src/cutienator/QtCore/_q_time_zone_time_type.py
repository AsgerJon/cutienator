"""
TimeType stands for the enum 'QTimeZone::TimeType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qtimezone.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TimeType(CuteNum):
  """
  The enum 'QTimeZone::TimeType' of Qt, with the 3 names Qt gives in it.
  """

  StandardTime = Kee[int](0)
  DaylightTime = Kee[int](1)
  GenericTime = Kee[int](2)
