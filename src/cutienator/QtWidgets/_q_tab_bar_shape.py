"""
Shape stands for the enum 'QTabBar::Shape' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qtabbar.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Shape(CuteNum):
  """
  The enum 'QTabBar::Shape' of Qt, with the 8 names Qt gives in it.
  """

  RoundedNorth = Kee[int](0)
  RoundedSouth = Kee[int](1)
  RoundedWest = Kee[int](2)
  RoundedEast = Kee[int](3)
  TriangularNorth = Kee[int](4)
  TriangularSouth = Kee[int](5)
  TriangularWest = Kee[int](6)
  TriangularEast = Kee[int](7)
