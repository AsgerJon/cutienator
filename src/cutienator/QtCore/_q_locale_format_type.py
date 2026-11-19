"""
FormatType stands for the enum 'QLocale::FormatType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qlocale.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class FormatType(CuteNum):
  """
  The enum 'QLocale::FormatType' of Qt, with the 3 names Qt gives in it.
  """

  LongFormat = Kee[int](0)
  ShortFormat = Kee[int](1)
  NarrowFormat = Kee[int](2)
