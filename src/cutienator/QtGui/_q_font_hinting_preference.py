"""
HintingPreference stands for the enum 'QFont::HintingPreference' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qfont.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class HintingPreference(CuteNum):
  """
  The enum 'QFont::HintingPreference' of Qt, with the 4 names Qt gives in it.
  """

  PreferDefaultHinting = Kee[int](0)
  PreferNoHinting = Kee[int](1)
  PreferVerticalHinting = Kee[int](2)
  PreferFullHinting = Kee[int](3)
