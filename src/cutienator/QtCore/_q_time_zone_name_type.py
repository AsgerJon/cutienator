"""
NameType stands for the enum 'QTimeZone::NameType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qtimezone.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class NameType(CuteNum):
  """
  The enum 'QTimeZone::NameType' of Qt, with the 4 names Qt gives in it.
  """

  DefaultName = Kee[int](0)
  LongName = Kee[int](1)
  ShortName = Kee[int](2)
  OffsetName = Kee[int](3)
