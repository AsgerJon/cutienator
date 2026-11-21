"""
Reason stands for the enum 'QGraphicsSceneContextMenuEvent::Reason' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Reason(CuteNum):
  """
  The enum 'QGraphicsSceneContextMenuEvent::Reason' of Qt, with the 3 names
  Qt gives in it.
  """

  Mouse = Kee[int](0)
  Keyboard = Kee[int](1)
  Other = Kee[int](2)
