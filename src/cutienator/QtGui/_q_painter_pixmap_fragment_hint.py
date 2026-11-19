"""
PixmapFragmentHint stands for the flags enum 'QPainter::PixmapFragmentHint'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpainter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class PixmapFragmentHint(CuteFlags):
  """
  The flags enum 'QPainter::PixmapFragmentHint' of Qt, with the 1 names Qt
  gives in it. Qt names the type of its combinations
  'QPainter::PixmapFragmentHints'.
  """

  OpaqueHint = 0x1
