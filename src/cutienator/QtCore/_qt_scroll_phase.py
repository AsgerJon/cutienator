"""
ScrollPhase stands for the enum 'Qt::ScrollPhase' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ScrollPhase(CuteNum):
  """
  The enum 'Qt::ScrollPhase' of Qt, with the 5 names Qt gives in it.
  """

  NoScrollPhase = Kee[int](0)
  ScrollBegin = Kee[int](1)
  ScrollUpdate = Kee[int](2)
  ScrollEnd = Kee[int](3)
  ScrollMomentum = Kee[int](4)
