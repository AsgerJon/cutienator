"""
CacheModeFlag stands for the flags enum 'QGraphicsView::CacheModeFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgraphicsview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class CacheModeFlag(CuteFlags):
  """
  The flags enum 'QGraphicsView::CacheModeFlag' of Qt, with the 2 names Qt
  gives in it. Qt names the type of its combinations
  'QGraphicsView::CacheMode'.
  """

  CacheNone = 0x0
  CacheBackground = 0x1
