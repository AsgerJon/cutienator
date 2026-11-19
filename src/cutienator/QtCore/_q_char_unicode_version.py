"""
UnicodeVersion stands for the enum 'QChar::UnicodeVersion' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qchar.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class UnicodeVersion(CuteNum):
  """
  The enum 'QChar::UnicodeVersion' of Qt, with the 29 names Qt gives in it.
  """

  Unicode_Unassigned = Kee[int](0)
  Unicode_1_1 = Kee[int](1)
  Unicode_2_0 = Kee[int](2)
  Unicode_2_1_2 = Kee[int](3)
  Unicode_3_0 = Kee[int](4)
  Unicode_3_1 = Kee[int](5)
  Unicode_3_2 = Kee[int](6)
  Unicode_4_0 = Kee[int](7)
  Unicode_4_1 = Kee[int](8)
  Unicode_5_0 = Kee[int](9)
  Unicode_5_1 = Kee[int](10)
  Unicode_5_2 = Kee[int](11)
  Unicode_6_0 = Kee[int](12)
  Unicode_6_1 = Kee[int](13)
  Unicode_6_2 = Kee[int](14)
  Unicode_6_3 = Kee[int](15)
  Unicode_7_0 = Kee[int](16)
  Unicode_8_0 = Kee[int](17)
  Unicode_9_0 = Kee[int](18)
  Unicode_10_0 = Kee[int](19)
  Unicode_11_0 = Kee[int](20)
  Unicode_12_0 = Kee[int](21)
  Unicode_12_1 = Kee[int](22)
  Unicode_13_0 = Kee[int](23)
  Unicode_14_0 = Kee[int](24)
  Unicode_15_0 = Kee[int](25)
  Unicode_15_1 = Kee[int](26)
  Unicode_16_0 = Kee[int](27)
  Unicode_17_0 = Kee[int](28)
