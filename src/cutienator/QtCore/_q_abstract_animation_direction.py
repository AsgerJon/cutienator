"""
Direction stands for the enum 'QAbstractAnimation::Direction' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qabstractanimation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Direction(CuteNum):
  """
  The enum 'QAbstractAnimation::Direction' of Qt, with the 2 names Qt gives
  in it.
  """

  Forward = Kee[int](0)
  Backward = Kee[int](1)
