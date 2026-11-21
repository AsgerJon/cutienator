"""
StringFormat stands for the enum 'QUuid::StringFormat' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/quuid.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class StringFormat(CuteNum):
  """
  The enum 'QUuid::StringFormat' of Qt, with the 3 names Qt gives in it.
  """

  WithBraces = Kee[int](0)
  WithoutBraces = Kee[int](1)
  Id128 = Kee[int](3)
