"""
Spread stands for the enum 'QGradient::Spread' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qbrush.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Spread(CuteNum):
  """
  The enum 'QGradient::Spread' of Qt, with the 3 names Qt gives in it.
  """

  PadSpread = Kee[int](0)
  ReflectSpread = Kee[int](1)
  RepeatSpread = Kee[int](2)
