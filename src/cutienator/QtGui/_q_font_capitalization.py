"""
Capitalization stands for the enum 'QFont::Capitalization' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qfont.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Capitalization(CuteNum):
  """
  The enum 'QFont::Capitalization' of Qt, with the 5 names Qt gives in it.
  """

  MixedCase = Kee[int](0)
  AllUppercase = Kee[int](1)
  AllLowercase = Kee[int](2)
  SmallCaps = Kee[int](3)
  Capitalize = Kee[int](4)
