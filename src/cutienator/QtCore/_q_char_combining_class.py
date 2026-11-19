"""
CombiningClass stands for the enum 'QChar::CombiningClass' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qchar.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class CombiningClass(CuteNum):
  """
  The enum 'QChar::CombiningClass' of Qt, with the 19 names Qt gives in it.
  """

  Combining_BelowLeftAttached = Kee[int](200)
  Combining_BelowAttached = Kee[int](202)
  Combining_BelowRightAttached = Kee[int](204)
  Combining_LeftAttached = Kee[int](208)
  Combining_RightAttached = Kee[int](210)
  Combining_AboveLeftAttached = Kee[int](212)
  Combining_AboveAttached = Kee[int](214)
  Combining_AboveRightAttached = Kee[int](216)
  Combining_BelowLeft = Kee[int](218)
  Combining_Below = Kee[int](220)
  Combining_BelowRight = Kee[int](222)
  Combining_Left = Kee[int](224)
  Combining_Right = Kee[int](226)
  Combining_AboveLeft = Kee[int](228)
  Combining_Above = Kee[int](230)
  Combining_AboveRight = Kee[int](232)
  Combining_DoubleBelow = Kee[int](233)
  Combining_DoubleAbove = Kee[int](234)
  Combining_IotaSubscript = Kee[int](240)
