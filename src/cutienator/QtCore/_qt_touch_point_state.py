"""
TouchPointState stands for the flags enum 'Qt::TouchPointState' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class TouchPointState(CuteFlags):
  """
  The flags enum 'Qt::TouchPointState' of Qt, with the 5 names Qt gives in
  it. Qt names the type of its combinations 'Qt::TouchPointStates'.
  """

  TouchPointUnknownState = 0x0
  TouchPointPressed = 0x1
  TouchPointMoved = 0x2
  TouchPointStationary = 0x4
  TouchPointReleased = 0x8
