"""
RenderableType stands for the enum 'QSurfaceFormat::RenderableType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qsurfaceformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class RenderableType(CuteNum):
  """
  The enum 'QSurfaceFormat::RenderableType' of Qt, with the 4 names Qt gives
  in it.
  """

  DefaultRenderableType = Kee[int](0)
  OpenGL = Kee[int](1)
  OpenGLES = Kee[int](2)
  OpenVG = Kee[int](4)
