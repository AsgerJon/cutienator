"""
ArrowType stands for the enum 'Qt::ArrowType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ArrowType(CuteNum):
  """
  The enum 'Qt::ArrowType' of Qt, with the 5 names Qt gives in it.
  """

  NoArrow = Kee[int](0)
  UpArrow = Kee[int](1)
  DownArrow = Kee[int](2)
  LeftArrow = Kee[int](3)
  RightArrow = Kee[int](4)
