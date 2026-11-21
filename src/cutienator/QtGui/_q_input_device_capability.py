"""
Capability stands for the flags enum 'QInputDevice::Capability' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qinputdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Capability(CuteFlags, scoped=True):
  """
  The flags enum 'QInputDevice::Capability' of Qt, with the 16 names Qt gives
  in it. Qt names the type of its combinations 'QInputDevice::Capabilities'.
  C++ keeps these names inside the enum, so the class that holds the enum
  does not have them.
  """

  NULL = 0x0
  Position = 0x1
  Area = 0x2
  Pressure = 0x4
  Velocity = 0x8
  NormalizedPosition = 0x20
  MouseEmulation = 0x40
  PixelScroll = 0x80
  Scroll = 0x100
  Hover = 0x200
  Rotation = 0x400
  XTilt = 0x800
  YTilt = 0x1000
  TangentialPressure = 0x2000
  ZPosition = 0x4000
  All = 0x7fffffff
