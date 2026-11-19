"""
GlyphRunRetrievalFlag stands for the flags enum
'QTextLayout::GlyphRunRetrievalFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class GlyphRunRetrievalFlag(CuteFlags, number='unsigned short'):
  """
  The flags enum 'QTextLayout::GlyphRunRetrievalFlag' of Qt, with the 6 names
  Qt gives in it. Qt names the type of its combinations
  'QTextLayout::GlyphRunRetrievalFlags'.
  """

  RetrieveGlyphIndexes = 0x1
  RetrieveGlyphPositions = 0x2
  RetrieveStringIndexes = 0x4
  RetrieveString = 0x8
  DefaultRetrievalFlags = 0x3
  RetrieveAll = 0xffff
