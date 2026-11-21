"""
DeviceType stands for the flags enum 'QInputDevice::DeviceType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qinputdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class DeviceType(CuteFlags, scoped=True):
  """
  The flags enum 'QInputDevice::DeviceType' of Qt, with the 9 names Qt gives
  in it. Qt names the type of its combinations 'QInputDevice::DeviceTypes'.
  C++ keeps these names inside the enum, so the class that holds the enum
  does not have them.
  """

  Unknown = 0x0
  Mouse = 0x1
  TouchScreen = 0x2
  TouchPad = 0x4
  Puck = 0x8
  Stylus = 0x10
  Airbrush = 0x20
  Keyboard = 0x1000
  AllDevices = 0x7fffffff
