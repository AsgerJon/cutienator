"""
Axis stands for the enum 'Qt::Axis' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Axis(CuteNum):
  """
  The enum 'Qt::Axis' of Qt, with the 3 names Qt gives in it.
  """

  XAxis = Kee[int](0)
  YAxis = Kee[int](1)
  ZAxis = Kee[int](2)
