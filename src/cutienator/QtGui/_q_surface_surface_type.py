"""
SurfaceType stands for the enum 'QSurface::SurfaceType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qsurface.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SurfaceType(CuteNum):
  """
  The enum 'QSurface::SurfaceType' of Qt, with the 7 names Qt gives in it.
  """

  RasterSurface = Kee[int](0)
  OpenGLSurface = Kee[int](1)
  RasterGLSurface = Kee[int](2)
  OpenVGSurface = Kee[int](3)
  VulkanSurface = Kee[int](4)
  MetalSurface = Kee[int](5)
  Direct3DSurface = Kee[int](6)
