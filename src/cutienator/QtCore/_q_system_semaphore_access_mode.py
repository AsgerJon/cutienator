"""
AccessMode stands for the enum 'QSystemSemaphore::AccessMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qsystemsemaphore.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class AccessMode(CuteNum):
  """
  The enum 'QSystemSemaphore::AccessMode' of Qt, with the 2 names Qt gives in
  it.
  """

  Open = Kee[int](0)
  Create = Kee[int](1)
