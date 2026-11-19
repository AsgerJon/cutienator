"""
FileError stands for the enum 'QFileDevice::FileError' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qfiledevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class FileError(CuteNum):
  """
  The enum 'QFileDevice::FileError' of Qt, with the 15 names Qt gives in it.
  """

  NoError = Kee[int](0)
  ReadError = Kee[int](1)
  WriteError = Kee[int](2)
  FatalError = Kee[int](3)
  ResourceError = Kee[int](4)
  OpenError = Kee[int](5)
  AbortError = Kee[int](6)
  TimeOutError = Kee[int](7)
  UnspecifiedError = Kee[int](8)
  RemoveError = Kee[int](9)
  RenameError = Kee[int](10)
  PositionError = Kee[int](11)
  ResizeError = Kee[int](12)
  PermissionsError = Kee[int](13)
  CopyError = Kee[int](14)
