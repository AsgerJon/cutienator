"""
DockWidgetArea stands for the flags enum 'Qt::DockWidgetArea' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class DockWidgetArea(CuteFlags):
  """
  The flags enum 'Qt::DockWidgetArea' of Qt, with the 7 names Qt gives in it.
  Qt names the type of its combinations 'Qt::DockWidgetAreas'.
  """

  LeftDockWidgetArea = 0x1
  RightDockWidgetArea = 0x2
  TopDockWidgetArea = 0x4
  BottomDockWidgetArea = 0x8
  DockWidgetArea_Mask = 0xf
  AllDockWidgetAreas = 0xf
  NoDockWidgetArea = 0x0
