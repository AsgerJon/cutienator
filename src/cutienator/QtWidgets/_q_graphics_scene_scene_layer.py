"""
SceneLayer stands for the flags enum 'QGraphicsScene::SceneLayer' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgraphicsscene.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class SceneLayer(CuteFlags):
  """
  The flags enum 'QGraphicsScene::SceneLayer' of Qt, with the 4 names Qt
  gives in it. Qt names the type of its combinations
  'QGraphicsScene::SceneLayers'.
  """

  ItemLayer = 0x1
  BackgroundLayer = 0x2
  ForegroundLayer = 0x4
  AllLayers = 0xffff
