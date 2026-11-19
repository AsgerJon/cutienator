"""
ItemIndexMethod stands for the enum 'QGraphicsScene::ItemIndexMethod' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgraphicsscene.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ItemIndexMethod(CuteNum):
  """
  The enum 'QGraphicsScene::ItemIndexMethod' of Qt, with the 2 names Qt gives
  in it.
  """

  BspTreeIndex = Kee[int](0)
  NoIndex = Kee[int](-1)
