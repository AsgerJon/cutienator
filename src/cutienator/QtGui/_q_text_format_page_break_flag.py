"""
PageBreakFlag stands for the flags enum 'QTextFormat::PageBreakFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class PageBreakFlag(CuteFlags):
  """
  The flags enum 'QTextFormat::PageBreakFlag' of Qt, with the 3 names Qt
  gives in it. Qt names the type of its combinations
  'QTextFormat::PageBreakFlags'.
  """

  PageBreak_Auto = 0x0
  PageBreak_AlwaysBefore = 0x1
  PageBreak_AlwaysAfter = 0x10
