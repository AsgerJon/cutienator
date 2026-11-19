"""
EventPriority stands for the enum 'Qt::EventPriority' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class EventPriority(CuteNum):
  """
  The enum 'Qt::EventPriority' of Qt, with the 3 names Qt gives in it.
  """

  HighEventPriority = Kee[int](1)
  NormalEventPriority = Kee[int](0)
  LowEventPriority = Kee[int](-1)
