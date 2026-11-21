"""
LockError stands for the enum 'QLockFile::LockError' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qlockfile.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class LockError(CuteNum):
  """
  The enum 'QLockFile::LockError' of Qt, with the 4 names Qt gives in it.
  """

  NoError = Kee[int](0)
  LockFailedError = Kee[int](1)
  PermissionError = Kee[int](2)
  UnknownError = Kee[int](3)
