"""
State stands for the enum 'QAbstractAnimation::State' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qabstractanimation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class State(CuteNum):
  """
  The enum 'QAbstractAnimation::State' of Qt, with the 3 names Qt gives in
  it.
  """

  Stopped = Kee[int](0)
  Paused = Kee[int](1)
  Running = Kee[int](2)
