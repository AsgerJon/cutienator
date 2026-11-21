"""
SystemSemaphoreError stands for the enum
'QSystemSemaphore::SystemSemaphoreError' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qsystemsemaphore.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SystemSemaphoreError(CuteNum):
  """
  The enum 'QSystemSemaphore::SystemSemaphoreError' of Qt, with the 7 names
  Qt gives in it.
  """

  NoError = Kee[int](0)
  PermissionDenied = Kee[int](1)
  KeyError = Kee[int](2)
  AlreadyExists = Kee[int](3)
  NotFound = Kee[int](4)
  OutOfResources = Kee[int](5)
  UnknownError = Kee[int](6)
