"""
PenJoinStyle stands for the enum 'Qt::PenJoinStyle' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class PenJoinStyle(CuteNum):
  """
  The enum 'Qt::PenJoinStyle' of Qt, with the 5 names Qt gives in it.
  """

  MiterJoin = Kee[int](0)
  BevelJoin = Kee[int](64)
  RoundJoin = Kee[int](128)
  SvgMiterJoin = Kee[int](256)
  MPenJoinStyle = Kee[int](448)
