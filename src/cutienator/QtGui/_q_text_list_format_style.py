"""
Style stands for the enum 'QTextListFormat::Style' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Style(CuteNum):
  """
  The enum 'QTextListFormat::Style' of Qt, with the 9 names Qt gives in it.
  """

  ListDisc = Kee[int](-1)
  ListCircle = Kee[int](-2)
  ListSquare = Kee[int](-3)
  ListDecimal = Kee[int](-4)
  ListLowerAlpha = Kee[int](-5)
  ListUpperAlpha = Kee[int](-6)
  ListLowerRoman = Kee[int](-7)
  ListUpperRoman = Kee[int](-8)
  ListStyleUndefined = Kee[int](0)
