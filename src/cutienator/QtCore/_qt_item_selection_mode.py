"""
ItemSelectionMode stands for the enum 'Qt::ItemSelectionMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ItemSelectionMode(CuteNum):
  """
  The enum 'Qt::ItemSelectionMode' of Qt, with the 4 names Qt gives in it.
  """

  ContainsItemShape = Kee[int](0)
  IntersectsItemShape = Kee[int](1)
  ContainsItemBoundingRect = Kee[int](2)
  IntersectsItemBoundingRect = Kee[int](3)
