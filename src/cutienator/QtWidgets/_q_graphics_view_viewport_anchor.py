"""
ViewportAnchor stands for the enum 'QGraphicsView::ViewportAnchor' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgraphicsview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ViewportAnchor(CuteNum):
  """
  The enum 'QGraphicsView::ViewportAnchor' of Qt, with the 3 names Qt gives
  in it.
  """

  NoAnchor = Kee[int](0)
  AnchorViewCenter = Kee[int](1)
  AnchorUnderMouse = Kee[int](2)
