"""
RecursionMode stands for the enum 'QReadWriteLock::RecursionMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qreadwritelock.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class RecursionMode(CuteNum):
  """
  The enum 'QReadWriteLock::RecursionMode' of Qt, with the 2 names Qt gives
  in it.
  """

  NonRecursive = Kee[int](0)
  Recursive = Kee[int](1)
