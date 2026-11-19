"""
ViewportUpdateMode stands for the enum 'QGraphicsView::ViewportUpdateMode' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgraphicsview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ViewportUpdateMode(CuteNum):
  """
  The enum 'QGraphicsView::ViewportUpdateMode' of Qt, with the 5 names Qt
  gives in it.
  """

  FullViewportUpdate = Kee[int](0)
  MinimalViewportUpdate = Kee[int](1)
  SmartViewportUpdate = Kee[int](2)
  NoViewportUpdate = Kee[int](3)
  BoundingRectViewportUpdate = Kee[int](4)
