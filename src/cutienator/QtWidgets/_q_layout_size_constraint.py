"""
SizeConstraint stands for the enum 'QLayout::SizeConstraint' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SizeConstraint(CuteNum):
  """
  The enum 'QLayout::SizeConstraint' of Qt, with the 6 names Qt gives in it.
  """

  SetDefaultConstraint = Kee[int](0)
  SetNoConstraint = Kee[int](1)
  SetMinimumSize = Kee[int](2)
  SetFixedSize = Kee[int](3)
  SetMaximumSize = Kee[int](4)
  SetMinAndMaxSize = Kee[int](5)
