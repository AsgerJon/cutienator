"""
AnchorPoint stands for the enum 'Qt::AnchorPoint' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class AnchorPoint(CuteNum):
  """
  The enum 'Qt::AnchorPoint' of Qt, with the 6 names Qt gives in it.
  """

  AnchorLeft = Kee[int](0)
  AnchorHorizontalCenter = Kee[int](1)
  AnchorRight = Kee[int](2)
  AnchorTop = Kee[int](3)
  AnchorVerticalCenter = Kee[int](4)
  AnchorBottom = Kee[int](5)
