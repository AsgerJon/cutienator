"""
WrapMode stands for the enum 'QTextOption::WrapMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class WrapMode(CuteNum):
  """
  The enum 'QTextOption::WrapMode' of Qt, with the 5 names Qt gives in it.
  """

  NoWrap = Kee[int](0)
  WordWrap = Kee[int](1)
  ManualWrap = Kee[int](2)
  WrapAnywhere = Kee[int](3)
  WrapAtWordBoundaryOrAnywhere = Kee[int](4)
