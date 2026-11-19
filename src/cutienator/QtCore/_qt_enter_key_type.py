"""
EnterKeyType stands for the enum 'Qt::EnterKeyType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class EnterKeyType(CuteNum):
  """
  The enum 'Qt::EnterKeyType' of Qt, with the 8 names Qt gives in it.
  """

  EnterKeyDefault = Kee[int](0)
  EnterKeyReturn = Kee[int](1)
  EnterKeyDone = Kee[int](2)
  EnterKeyGo = Kee[int](3)
  EnterKeySend = Kee[int](4)
  EnterKeySearch = Kee[int](5)
  EnterKeyNext = Kee[int](6)
  EnterKeyPrevious = Kee[int](7)
