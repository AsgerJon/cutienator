"""
DirtyFlag stands for the flags enum 'QPaintEngine::DirtyFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpaintengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class DirtyFlag(CuteFlags):
  """
  The flags enum 'QPaintEngine::DirtyFlag' of Qt, with the 14 names Qt gives
  in it. Qt names the type of its combinations 'QPaintEngine::DirtyFlags'.
  """

  DirtyPen = 0x1
  DirtyBrush = 0x2
  DirtyBrushOrigin = 0x4
  DirtyFont = 0x8
  DirtyBackground = 0x10
  DirtyBackgroundMode = 0x20
  DirtyTransform = 0x40
  DirtyClipRegion = 0x80
  DirtyClipPath = 0x100
  DirtyHints = 0x200
  DirtyCompositionMode = 0x400
  DirtyClipEnabled = 0x800
  DirtyOpacity = 0x1000
  AllDirty = 0xffff
