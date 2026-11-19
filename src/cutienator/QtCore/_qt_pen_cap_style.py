"""
PenCapStyle stands for the enum 'Qt::PenCapStyle' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class PenCapStyle(CuteNum):
  """
  The enum 'Qt::PenCapStyle' of Qt, with the 4 names Qt gives in it.
  """

  FlatCap = Kee[int](0)
  SquareCap = Kee[int](16)
  RoundCap = Kee[int](32)
  MPenCapStyle = Kee[int](48)
