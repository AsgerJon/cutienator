"""
PaintEngineFeature stands for the flags enum
'QPaintEngine::PaintEngineFeature' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpaintengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class PaintEngineFeature(CuteFlags, number='unsigned int'):
  """
  The flags enum 'QPaintEngine::PaintEngineFeature' of Qt, with the 20 names
  Qt gives in it. Qt names the type of its combinations
  'QPaintEngine::PaintEngineFeatures'.
  """

  PrimitiveTransform = 0x1
  PatternTransform = 0x2
  PixmapTransform = 0x4
  PatternBrush = 0x8
  LinearGradientFill = 0x10
  RadialGradientFill = 0x20
  ConicalGradientFill = 0x40
  AlphaBlend = 0x80
  PorterDuff = 0x100
  PainterPaths = 0x200
  Antialiasing = 0x400
  BrushStroke = 0x800
  ConstantOpacity = 0x1000
  MaskedBrush = 0x2000
  PerspectiveTransform = 0x4000
  BlendModes = 0x8000
  ObjectBoundingModeGradients = 0x10000
  RasterOpModes = 0x20000
  PaintOutsidePaintEvent = 0x20000000
  AllFeatures = 0xffffffff
