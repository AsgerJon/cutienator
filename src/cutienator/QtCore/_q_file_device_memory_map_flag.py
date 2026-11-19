"""
MemoryMapFlag stands for the flags enum 'QFileDevice::MemoryMapFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qfiledevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class MemoryMapFlag(CuteFlags):
  """
  The flags enum 'QFileDevice::MemoryMapFlag' of Qt, with the 2 names Qt
  gives in it. Qt names the type of its combinations
  'QFileDevice::MemoryMapFlags'.
  """

  NoOptions = 0x0
  MapPrivateOption = 0x1
