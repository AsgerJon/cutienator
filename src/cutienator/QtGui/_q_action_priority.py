"""
Priority stands for the enum 'QAction::Priority' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qaction.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Priority(CuteNum):
  """
  The enum 'QAction::Priority' of Qt, with the 3 names Qt gives in it.
  """

  LowPriority = Kee[int](0)
  NormalPriority = Kee[int](128)
  HighPriority = Kee[int](256)
