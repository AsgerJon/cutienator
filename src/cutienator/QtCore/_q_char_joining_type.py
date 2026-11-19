"""
JoiningType stands for the enum 'QChar::JoiningType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qchar.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class JoiningType(CuteNum):
  """
  The enum 'QChar::JoiningType' of Qt, with the 6 names Qt gives in it.
  """

  Joining_None = Kee[int](0)
  Joining_Causing = Kee[int](1)
  Joining_Dual = Kee[int](2)
  Joining_Right = Kee[int](3)
  Joining_Left = Kee[int](4)
  Joining_Transparent = Kee[int](5)
