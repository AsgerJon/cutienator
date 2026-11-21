"""
PixmapPadMode stands for the enum 'QGraphicsEffect::PixmapPadMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class PixmapPadMode(CuteNum):
  """
  The enum 'QGraphicsEffect::PixmapPadMode' of Qt, with the 3 names Qt gives
  in it.
  """

  NoPad = Kee[int](0)
  PadToTransparentBorder = Kee[int](1)
  PadToEffectiveBoundingRect = Kee[int](2)
