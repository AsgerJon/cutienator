"""
SwapBehavior stands for the enum 'QSurfaceFormat::SwapBehavior' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qsurfaceformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SwapBehavior(CuteNum):
  """
  The enum 'QSurfaceFormat::SwapBehavior' of Qt, with the 4 names Qt gives in
  it.
  """

  DefaultSwapBehavior = Kee[int](0)
  SingleBuffer = Kee[int](1)
  DoubleBuffer = Kee[int](2)
  TripleBuffer = Kee[int](3)
