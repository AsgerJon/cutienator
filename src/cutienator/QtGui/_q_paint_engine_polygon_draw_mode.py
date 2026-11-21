"""
PolygonDrawMode stands for the enum 'QPaintEngine::PolygonDrawMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpaintengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class PolygonDrawMode(CuteNum):
  """
  The enum 'QPaintEngine::PolygonDrawMode' of Qt, with the 4 names Qt gives
  in it.
  """

  OddEvenMode = Kee[int](0)
  WindingMode = Kee[int](1)
  ConvexMode = Kee[int](2)
  PolylineMode = Kee[int](3)
