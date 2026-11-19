"""
StyleHint stands for the enum 'QFont::StyleHint' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qfont.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class StyleHint(CuteNum):
  """
  The enum 'QFont::StyleHint' of Qt, with the 13 names Qt gives in it.
  """

  Helvetica = Kee[int](0)
  SansSerif = Kee[int](0)
  Times = Kee[int](1)
  Serif = Kee[int](1)
  Courier = Kee[int](2)
  TypeWriter = Kee[int](2)
  OldEnglish = Kee[int](3)
  Decorative = Kee[int](3)
  System = Kee[int](4)
  AnyStyle = Kee[int](5)
  Cursive = Kee[int](6)
  Monospace = Kee[int](7)
  Fantasy = Kee[int](8)
