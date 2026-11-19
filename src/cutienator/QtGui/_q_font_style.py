"""
Style stands for the enum 'QFont::Style' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qfont.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Style(CuteNum):
  """
  The enum 'QFont::Style' of Qt, with the 3 names Qt gives in it.
  """

  StyleNormal = Kee[int](0)
  StyleItalic = Kee[int](1)
  StyleOblique = Kee[int](2)
