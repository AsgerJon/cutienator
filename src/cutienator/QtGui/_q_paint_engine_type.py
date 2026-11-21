"""
Type stands for the enum 'QPaintEngine::Type' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpaintengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Type(CuteNum):
  """
  The enum 'QPaintEngine::Type' of Qt, with the 19 names Qt gives in it.
  """

  X11 = Kee[int](0)
  Windows = Kee[int](1)
  QuickDraw = Kee[int](2)
  CoreGraphics = Kee[int](3)
  MacPrinter = Kee[int](4)
  QWindowSystem = Kee[int](5)
  OpenGL = Kee[int](6)
  Picture = Kee[int](7)
  SVG = Kee[int](8)
  Raster = Kee[int](9)
  Direct3D = Kee[int](10)
  Pdf = Kee[int](11)
  OpenVG = Kee[int](12)
  OpenGL2 = Kee[int](13)
  PaintBuffer = Kee[int](14)
  Blitter = Kee[int](15)
  Direct2D = Kee[int](16)
  User = Kee[int](50)
  MaxUser = Kee[int](100)
