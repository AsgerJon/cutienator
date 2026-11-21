"""
PointerType stands for the flags enum 'QPointingDevice::PointerType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpointingdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class PointerType(CuteFlags, scoped=True):
  """
  The flags enum 'QPointingDevice::PointerType' of Qt, with the 8 names Qt
  gives in it. Qt names the type of its combinations
  'QPointingDevice::PointerTypes'. C++ keeps these names inside the enum, so
  the class that holds the enum does not have them.
  """

  Unknown = 0x0
  Generic = 0x1
  Finger = 0x2
  Pen = 0x4
  Eraser = 0x8
  Cursor = 0x10
  Palm = 0x20
  AllPointerTypes = 0x7fff
