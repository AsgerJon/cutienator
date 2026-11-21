"""
GraphicsItemChange stands for the enum 'QGraphicsItem::GraphicsItemChange' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class GraphicsItemChange(CuteNum):
  """
  The enum 'QGraphicsItem::GraphicsItemChange' of Qt, with the 33 names Qt
  gives in it.
  """

  ItemPositionChange = Kee[int](0)
  ItemVisibleChange = Kee[int](2)
  ItemEnabledChange = Kee[int](3)
  ItemSelectedChange = Kee[int](4)
  ItemParentChange = Kee[int](5)
  ItemChildAddedChange = Kee[int](6)
  ItemChildRemovedChange = Kee[int](7)
  ItemTransformChange = Kee[int](8)
  ItemPositionHasChanged = Kee[int](9)
  ItemTransformHasChanged = Kee[int](10)
  ItemSceneChange = Kee[int](11)
  ItemVisibleHasChanged = Kee[int](12)
  ItemEnabledHasChanged = Kee[int](13)
  ItemSelectedHasChanged = Kee[int](14)
  ItemParentHasChanged = Kee[int](15)
  ItemSceneHasChanged = Kee[int](16)
  ItemCursorChange = Kee[int](17)
  ItemCursorHasChanged = Kee[int](18)
  ItemToolTipChange = Kee[int](19)
  ItemToolTipHasChanged = Kee[int](20)
  ItemFlagsChange = Kee[int](21)
  ItemFlagsHaveChanged = Kee[int](22)
  ItemZValueChange = Kee[int](23)
  ItemZValueHasChanged = Kee[int](24)
  ItemOpacityChange = Kee[int](25)
  ItemOpacityHasChanged = Kee[int](26)
  ItemScenePositionHasChanged = Kee[int](27)
  ItemRotationChange = Kee[int](28)
  ItemRotationHasChanged = Kee[int](29)
  ItemScaleChange = Kee[int](30)
  ItemScaleHasChanged = Kee[int](31)
  ItemTransformOriginPointChange = Kee[int](32)
  ItemTransformOriginPointHasChanged = Kee[int](33)
