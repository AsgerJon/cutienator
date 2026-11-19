"""
DragMode stands for the enum 'QGraphicsView::DragMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgraphicsview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class DragMode(CuteNum):
  """
  The enum 'QGraphicsView::DragMode' of Qt, with the 3 names Qt gives in it.
  """

  NoDrag = Kee[int](0)
  ScrollHandDrag = Kee[int](1)
  RubberBandDrag = Kee[int](2)
