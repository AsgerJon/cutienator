"""
DateFormat stands for the enum 'Qt::DateFormat' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class DateFormat(CuteNum):
  """
  The enum 'Qt::DateFormat' of Qt, with the 4 names Qt gives in it.
  """

  TextDate = Kee[int](0)
  ISODate = Kee[int](1)
  RFC2822Date = Kee[int](8)
  ISODateWithMs = Kee[int](9)
