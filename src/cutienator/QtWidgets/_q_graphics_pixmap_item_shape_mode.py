"""
ShapeMode stands for the enum 'QGraphicsPixmapItem::ShapeMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ShapeMode(CuteNum):
  """
  The enum 'QGraphicsPixmapItem::ShapeMode' of Qt, with the 3 names Qt gives
  in it.
  """

  MaskShape = Kee[int](0)
  BoundingRectShape = Kee[int](1)
  HeuristicMaskShape = Kee[int](2)
