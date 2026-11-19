"""
BrushStyle stands for the enum 'Qt::BrushStyle' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class BrushStyle(CuteNum):
  """
  The enum 'Qt::BrushStyle' of Qt, with the 19 names Qt gives in it.
  """

  NoBrush = Kee[int](0)
  SolidPattern = Kee[int](1)
  Dense1Pattern = Kee[int](2)
  Dense2Pattern = Kee[int](3)
  Dense3Pattern = Kee[int](4)
  Dense4Pattern = Kee[int](5)
  Dense5Pattern = Kee[int](6)
  Dense6Pattern = Kee[int](7)
  Dense7Pattern = Kee[int](8)
  HorPattern = Kee[int](9)
  VerPattern = Kee[int](10)
  CrossPattern = Kee[int](11)
  BDiagPattern = Kee[int](12)
  FDiagPattern = Kee[int](13)
  DiagCrossPattern = Kee[int](14)
  LinearGradientPattern = Kee[int](15)
  RadialGradientPattern = Kee[int](16)
  ConicalGradientPattern = Kee[int](17)
  TexturePattern = Kee[int](24)
