"""
WindowState stands for the flags enum 'Qt::WindowState' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class WindowState(CuteFlags):
  """
  The flags enum 'Qt::WindowState' of Qt, with the 5 names Qt gives in it. Qt
  names the type of its combinations 'Qt::WindowStates'.
  """

  WindowNoState = 0x0
  WindowMinimized = 0x1
  WindowMaximized = 0x2
  WindowFullScreen = 0x4
  WindowActive = 0x8
