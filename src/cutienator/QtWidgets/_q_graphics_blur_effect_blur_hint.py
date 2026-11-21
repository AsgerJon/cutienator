"""
BlurHint stands for the flags enum 'QGraphicsBlurEffect::BlurHint' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class BlurHint(CuteFlags):
  """
  The flags enum 'QGraphicsBlurEffect::BlurHint' of Qt, with the 3 names Qt
  gives in it. Qt names the type of its combinations
  'QGraphicsBlurEffect::BlurHints'.
  """

  PerformanceHint = 0x0
  QualityHint = 0x1
  AnimationHint = 0x2
