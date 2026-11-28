"""
QDrawBorderPixmap stands for the namespace 'QQC2::QDrawBorderPixmap' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class QDrawBorderPixmap:
  """
  The namespace 'QQC2::QDrawBorderPixmap' of Qt, which holds no objects. It
  holds the 1 enums Qt writes in it, each under its name, and the 1 names Qt
  has for the combinations of a flags enum, each holding the class of that
  enum. It is never made into an object.
  """

  class DrawingHint(CuteFlags):
    """
    The flags enum 'QQC2::QDrawBorderPixmap::DrawingHint' of Qt, with the 13
    names Qt gives in it. Qt names the type of its combinations
    'QQC2::QDrawBorderPixmap::DrawingHints'.
    """

    OpaqueTopLeft = 0x1
    OpaqueTop = 0x2
    OpaqueTopRight = 0x4
    OpaqueLeft = 0x8
    OpaqueCenter = 0x10
    OpaqueRight = 0x20
    OpaqueBottomLeft = 0x40
    OpaqueBottom = 0x80
    OpaqueBottomRight = 0x100
    OpaqueCorners = 0x145
    OpaqueEdges = 0xaa
    OpaqueFrame = 0x1ef
    OpaqueAll = 0x1ff

  DrawingHints = DrawingHint
