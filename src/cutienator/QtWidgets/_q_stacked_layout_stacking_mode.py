"""
StackingMode stands for the enum 'QStackedLayout::StackingMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstackedlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class StackingMode(CuteNum):
  """
  The enum 'QStackedLayout::StackingMode' of Qt, with the 2 names Qt gives in
  it.
  """

  StackOne = Kee[int](0)
  StackAll = Kee[int](1)
