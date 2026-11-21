"""
Variant stands for the enum 'QUuid::Variant' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/quuid.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Variant(CuteNum):
  """
  The enum 'QUuid::Variant' of Qt, with the 5 names Qt gives in it.
  """

  VarUnknown = Kee[int](-1)
  NCS = Kee[int](0)
  DCE = Kee[int](2)
  Microsoft = Kee[int](6)
  Reserved = Kee[int](7)
