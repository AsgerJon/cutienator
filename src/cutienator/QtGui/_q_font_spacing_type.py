"""
SpacingType stands for the enum 'QFont::SpacingType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qfont.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SpacingType(CuteNum):
  """
  The enum 'QFont::SpacingType' of Qt, with the 2 names Qt gives in it.
  """

  PercentageSpacing = Kee[int](0)
  AbsoluteSpacing = Kee[int](1)
