"""
RenderHint stands for the flags enum 'QPainter::RenderHint' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpainter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class RenderHint(CuteFlags):
  """
  The flags enum 'QPainter::RenderHint' of Qt, with the 6 names Qt gives in
  it. Qt names the type of its combinations 'QPainter::RenderHints'.
  """

  Antialiasing = 0x1
  TextAntialiasing = 0x2
  SmoothPixmapTransform = 0x4
  VerticalSubpixelPositioning = 0x8
  LosslessImageRendering = 0x40
  NonCosmeticBrushPatterns = 0x80
