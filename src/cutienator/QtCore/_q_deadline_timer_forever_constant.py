"""
ForeverConstant stands for the enum 'QDeadlineTimer::ForeverConstant' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qdeadlinetimer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ForeverConstant(CuteNum, scoped=True):
  """
  The enum 'QDeadlineTimer::ForeverConstant' of Qt, with the 1 names Qt gives
  in it. C++ keeps these names inside the enum, so the class that holds the
  enum does not have them.
  """

  Forever = Kee[int](0)
