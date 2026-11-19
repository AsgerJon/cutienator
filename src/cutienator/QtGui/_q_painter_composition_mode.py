"""
CompositionMode stands for the enum 'QPainter::CompositionMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpainter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class CompositionMode(CuteNum):
  """
  The enum 'QPainter::CompositionMode' of Qt, with the 39 names Qt gives in
  it.
  """

  CompositionMode_SourceOver = Kee[int](0)
  CompositionMode_DestinationOver = Kee[int](1)
  CompositionMode_Clear = Kee[int](2)
  CompositionMode_Source = Kee[int](3)
  CompositionMode_Destination = Kee[int](4)
  CompositionMode_SourceIn = Kee[int](5)
  CompositionMode_DestinationIn = Kee[int](6)
  CompositionMode_SourceOut = Kee[int](7)
  CompositionMode_DestinationOut = Kee[int](8)
  CompositionMode_SourceAtop = Kee[int](9)
  CompositionMode_DestinationAtop = Kee[int](10)
  CompositionMode_Xor = Kee[int](11)
  CompositionMode_Plus = Kee[int](12)
  CompositionMode_Multiply = Kee[int](13)
  CompositionMode_Screen = Kee[int](14)
  CompositionMode_Overlay = Kee[int](15)
  CompositionMode_Darken = Kee[int](16)
  CompositionMode_Lighten = Kee[int](17)
  CompositionMode_ColorDodge = Kee[int](18)
  CompositionMode_ColorBurn = Kee[int](19)
  CompositionMode_HardLight = Kee[int](20)
  CompositionMode_SoftLight = Kee[int](21)
  CompositionMode_Difference = Kee[int](22)
  CompositionMode_Exclusion = Kee[int](23)
  RasterOp_SourceOrDestination = Kee[int](24)
  RasterOp_SourceAndDestination = Kee[int](25)
  RasterOp_SourceXorDestination = Kee[int](26)
  RasterOp_NotSourceAndNotDestination = Kee[int](27)
  RasterOp_NotSourceOrNotDestination = Kee[int](28)
  RasterOp_NotSourceXorDestination = Kee[int](29)
  RasterOp_NotSource = Kee[int](30)
  RasterOp_NotSourceAndDestination = Kee[int](31)
  RasterOp_SourceAndNotDestination = Kee[int](32)
  RasterOp_NotSourceOrDestination = Kee[int](33)
  RasterOp_SourceOrNotDestination = Kee[int](34)
  RasterOp_ClearDestination = Kee[int](35)
  RasterOp_SetDestination = Kee[int](36)
  RasterOp_NotDestination = Kee[int](37)
  NCompositionModes = Kee[int](38)
