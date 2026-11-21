"""
RenderFlag stands for the flags enum 'QTextItem::RenderFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpaintengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class RenderFlag(CuteFlags, number='unsigned int'):
  """
  The flags enum 'QTextItem::RenderFlag' of Qt, with the 5 names Qt gives in
  it. Qt names the type of its combinations 'QTextItem::RenderFlags'.
  """

  RightToLeft = 0x1
  Overline = 0x10
  Underline = 0x20
  StrikeOut = 0x40
  Dummy = 0xffffffff
