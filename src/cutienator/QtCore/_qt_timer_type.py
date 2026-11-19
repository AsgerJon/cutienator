"""
TimerType stands for the enum 'Qt::TimerType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TimerType(CuteNum):
  """
  The enum 'Qt::TimerType' of Qt, with the 3 names Qt gives in it.
  """

  PreciseTimer = Kee[int](0)
  CoarseTimer = Kee[int](1)
  VeryCoarseTimer = Kee[int](2)
