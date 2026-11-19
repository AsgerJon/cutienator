"""
UnderlineStyle stands for the enum 'QTextCharFormat::UnderlineStyle' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class UnderlineStyle(CuteNum):
  """
  The enum 'QTextCharFormat::UnderlineStyle' of Qt, with the 8 names Qt gives
  in it.
  """

  NoUnderline = Kee[int](0)
  SingleUnderline = Kee[int](1)
  DashUnderline = Kee[int](2)
  DotLine = Kee[int](3)
  DashDotLine = Kee[int](4)
  DashDotDotLine = Kee[int](5)
  WaveUnderline = Kee[int](6)
  SpellCheckUnderline = Kee[int](7)
