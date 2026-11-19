"""
OptimizationFlag stands for the flags enum 'QGraphicsView::OptimizationFlag'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgraphicsview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class OptimizationFlag(CuteFlags):
  """
  The flags enum 'QGraphicsView::OptimizationFlag' of Qt, with the 3 names Qt
  gives in it. Qt names the type of its combinations
  'QGraphicsView::OptimizationFlags'.
  """

  DontSavePainterState = 0x1
  DontAdjustForAntialiasing = 0x2
  IndirectPainting = 0x4
