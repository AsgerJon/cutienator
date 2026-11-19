"""
Permission stands for the flags enum 'QFileDevice::Permission' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qfiledevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Permission(CuteFlags):
  """
  The flags enum 'QFileDevice::Permission' of Qt, with the 12 names Qt gives
  in it. Qt names the type of its combinations 'QFileDevice::Permissions'.
  """

  ReadOwner = 0x4000
  WriteOwner = 0x2000
  ExeOwner = 0x1000
  ReadUser = 0x400
  WriteUser = 0x200
  ExeUser = 0x100
  ReadGroup = 0x40
  WriteGroup = 0x20
  ExeGroup = 0x10
  ReadOther = 0x4
  WriteOther = 0x2
  ExeOther = 0x1
