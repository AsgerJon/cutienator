"""
ToolBarArea stands for the flags enum 'Qt::ToolBarArea' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ToolBarArea(CuteFlags):
  """
  The flags enum 'Qt::ToolBarArea' of Qt, with the 7 names Qt gives in it. Qt
  names the type of its combinations 'Qt::ToolBarAreas'.
  """

  LeftToolBarArea = 0x1
  RightToolBarArea = 0x2
  TopToolBarArea = 0x4
  BottomToolBarArea = 0x8
  ToolBarArea_Mask = 0xf
  AllToolBarAreas = 0xf
  NoToolBarArea = 0x0
