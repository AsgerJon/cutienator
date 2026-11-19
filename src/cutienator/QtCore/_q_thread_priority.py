"""
Priority stands for the enum 'QThread::Priority' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qthread.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Priority(CuteNum):
  """
  The enum 'QThread::Priority' of Qt, with the 8 names Qt gives in it.
  """

  IdlePriority = Kee[int](0)
  LowestPriority = Kee[int](1)
  LowPriority = Kee[int](2)
  NormalPriority = Kee[int](3)
  HighPriority = Kee[int](4)
  HighestPriority = Kee[int](5)
  TimeCriticalPriority = Kee[int](6)
  InheritPriority = Kee[int](7)
