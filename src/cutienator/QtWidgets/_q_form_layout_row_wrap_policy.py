"""
RowWrapPolicy stands for the enum 'QFormLayout::RowWrapPolicy' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qformlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class RowWrapPolicy(CuteNum):
  """
  The enum 'QFormLayout::RowWrapPolicy' of Qt, with the 3 names Qt gives in
  it.
  """

  DontWrapRows = Kee[int](0)
  WrapLongRows = Kee[int](1)
  WrapAllRows = Kee[int](2)
