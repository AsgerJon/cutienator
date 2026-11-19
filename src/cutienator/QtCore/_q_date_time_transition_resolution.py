"""
TransitionResolution stands for the enum 'QDateTime::TransitionResolution' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qdatetime.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TransitionResolution(CuteNum, scoped=True):
  """
  The enum 'QDateTime::TransitionResolution' of Qt, with the 8 names Qt gives
  in it. C++ keeps these names inside the enum, so the class that holds the
  enum does not have them.
  """

  Reject = Kee[int](0)
  RelativeToBefore = Kee[int](1)
  RelativeToAfter = Kee[int](2)
  PreferBefore = Kee[int](3)
  PreferAfter = Kee[int](4)
  PreferStandard = Kee[int](5)
  PreferDaylightSaving = Kee[int](6)
  LegacyBehavior = Kee[int](1)
