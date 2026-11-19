"""
Weight stands for the enum 'QFont::Weight' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qfont.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Weight(CuteNum):
  """
  The enum 'QFont::Weight' of Qt, with the 9 names Qt gives in it.
  """

  Thin = Kee[int](100)
  ExtraLight = Kee[int](200)
  Light = Kee[int](300)
  Normal = Kee[int](400)
  Medium = Kee[int](500)
  DemiBold = Kee[int](600)
  Bold = Kee[int](700)
  ExtraBold = Kee[int](800)
  Black = Kee[int](900)
