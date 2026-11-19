"""
GestureState stands for the enum 'Qt::GestureState' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class GestureState(CuteNum):
  """
  The enum 'Qt::GestureState' of Qt, with the 5 names Qt gives in it.
  """

  NoGesture = Kee[int](0)
  GestureStarted = Kee[int](1)
  GestureUpdated = Kee[int](2)
  GestureFinished = Kee[int](3)
  GestureCanceled = Kee[int](4)
