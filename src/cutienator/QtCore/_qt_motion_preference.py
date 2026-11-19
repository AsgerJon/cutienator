"""
MotionPreference stands for the enum 'Qt::MotionPreference' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MotionPreference(CuteNum, scoped=True):
  """
  The enum 'Qt::MotionPreference' of Qt, with the 2 names Qt gives in it. C++
  keeps these names inside the enum, so the class that holds the enum does
  not have them.
  """

  NoPreference = Kee[int](0)
  ReducedMotion = Kee[int](1)
