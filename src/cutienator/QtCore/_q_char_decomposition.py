"""
Decomposition stands for the enum 'QChar::Decomposition' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qchar.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Decomposition(CuteNum):
  """
  The enum 'QChar::Decomposition' of Qt, with the 18 names Qt gives in it.
  """

  NoDecomposition = Kee[int](0)
  Canonical = Kee[int](1)
  Font = Kee[int](2)
  NoBreak = Kee[int](3)
  Initial = Kee[int](4)
  Medial = Kee[int](5)
  Final = Kee[int](6)
  Isolated = Kee[int](7)
  Circle = Kee[int](8)
  Super = Kee[int](9)
  Sub = Kee[int](10)
  Vertical = Kee[int](11)
  Wide = Kee[int](12)
  Narrow = Kee[int](13)
  Small = Kee[int](14)
  Square = Kee[int](15)
  Compat = Kee[int](16)
  Fraction = Kee[int](17)
