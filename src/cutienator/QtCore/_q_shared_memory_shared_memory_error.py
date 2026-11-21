"""
SharedMemoryError stands for the enum 'QSharedMemory::SharedMemoryError' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qsharedmemory.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SharedMemoryError(CuteNum):
  """
  The enum 'QSharedMemory::SharedMemoryError' of Qt, with the 9 names Qt
  gives in it.
  """

  NoError = Kee[int](0)
  PermissionDenied = Kee[int](1)
  InvalidSize = Kee[int](2)
  KeyError = Kee[int](3)
  AlreadyExists = Kee[int](4)
  NotFound = Kee[int](5)
  LockError = Kee[int](6)
  OutOfResources = Kee[int](7)
  UnknownError = Kee[int](8)
