"""
ClockType stands for the enum 'QElapsedTimer::ClockType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qelapsedtimer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ClockType(CuteNum):
  """
  The enum 'QElapsedTimer::ClockType' of Qt, with the 5 names Qt gives in it.
  """

  SystemTime = Kee[int](0)
  MonotonicClock = Kee[int](1)
  TickCounter = Kee[int](2)
  MachAbsoluteTime = Kee[int](3)
  PerformanceCounter = Kee[int](4)
