"""
SystemFont stands for the enum 'QFontDatabase::SystemFont' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qfontdatabase.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SystemFont(CuteNum):
  """
  The enum 'QFontDatabase::SystemFont' of Qt, with the 4 names Qt gives in
  it.
  """

  GeneralFont = Kee[int](0)
  FixedFont = Kee[int](1)
  TitleFont = Kee[int](2)
  SmallestReadableFont = Kee[int](3)
