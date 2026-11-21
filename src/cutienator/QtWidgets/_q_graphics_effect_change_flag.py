"""
ChangeFlag stands for the flags enum 'QGraphicsEffect::ChangeFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ChangeFlag(CuteFlags):
  """
  The flags enum 'QGraphicsEffect::ChangeFlag' of Qt, with the 4 names Qt
  gives in it. Qt names the type of its combinations
  'QGraphicsEffect::ChangeFlags'.
  """

  SourceAttached = 0x1
  SourceDetached = 0x2
  SourceBoundingRectChanged = 0x4
  SourceInvalidated = 0x8
