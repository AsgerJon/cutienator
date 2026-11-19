"""
Edge stands for the flags enum 'Qt::Edge' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Edge(CuteFlags):
  """
  The flags enum 'Qt::Edge' of Qt, with the 4 names Qt gives in it. Qt names
  the type of its combinations 'Qt::Edges'.
  """

  TopEdge = 0x1
  LeftEdge = 0x2
  RightEdge = 0x4
  BottomEdge = 0x8
