"""
FileTime stands for the enum 'QFileDevice::FileTime' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qfiledevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class FileTime(CuteNum):
  """
  The enum 'QFileDevice::FileTime' of Qt, with the 4 names Qt gives in it.
  """

  FileAccessTime = Kee[int](0)
  FileBirthTime = Kee[int](1)
  FileMetadataChangeTime = Kee[int](2)
  FileModificationTime = Kee[int](3)
