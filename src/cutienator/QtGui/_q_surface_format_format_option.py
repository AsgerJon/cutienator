"""
FormatOption stands for the flags enum 'QSurfaceFormat::FormatOption' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qsurfaceformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class FormatOption(CuteFlags):
  """
  The flags enum 'QSurfaceFormat::FormatOption' of Qt, with the 5 names Qt
  gives in it. Qt names the type of its combinations
  'QSurfaceFormat::FormatOptions'.
  """

  StereoBuffers = 0x1
  DebugContext = 0x2
  DeprecatedFunctions = 0x4
  ResetNotification = 0x8
  ProtectedContent = 0x10
