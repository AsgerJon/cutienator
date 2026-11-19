"""
OpenModeFlag stands for the flags enum 'QIODeviceBase::OpenModeFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qiodevicebase.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class OpenModeFlag(CuteFlags):
  """
  The flags enum 'QIODeviceBase::OpenModeFlag' of Qt, with the 10 names Qt
  gives in it. Qt names the type of its combinations
  'QIODeviceBase::OpenMode'.
  """

  NotOpen = 0x0
  ReadOnly = 0x1
  WriteOnly = 0x2
  ReadWrite = 0x3
  Append = 0x4
  Truncate = 0x8
  Text = 0x10
  Unbuffered = 0x20
  NewOnly = 0x40
  ExistingOnly = 0x80
