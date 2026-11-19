"""
Stretch stands for the enum 'QFont::Stretch' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qfont.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Stretch(CuteNum):
  """
  The enum 'QFont::Stretch' of Qt, with the 10 names Qt gives in it.
  """

  AnyStretch = Kee[int](0)
  UltraCondensed = Kee[int](50)
  ExtraCondensed = Kee[int](62)
  Condensed = Kee[int](75)
  SemiCondensed = Kee[int](87)
  Unstretched = Kee[int](100)
  SemiExpanded = Kee[int](112)
  Expanded = Kee[int](125)
  ExtraExpanded = Kee[int](150)
  UltraExpanded = Kee[int](200)
