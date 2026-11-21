"""
OpenGLContextProfile stands for the enum
'QSurfaceFormat::OpenGLContextProfile' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qsurfaceformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class OpenGLContextProfile(CuteNum):
  """
  The enum 'QSurfaceFormat::OpenGLContextProfile' of Qt, with the 3 names Qt
  gives in it.
  """

  NoProfile = Kee[int](0)
  CoreProfile = Kee[int](1)
  CompatibilityProfile = Kee[int](2)
