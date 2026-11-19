"""
Type stands for the enum 'QGradient::Type' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qbrush.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Type(CuteNum):
  """
  The enum 'QGradient::Type' of Qt, with the 4 names Qt gives in it.
  """

  LinearGradient = Kee[int](0)
  RadialGradient = Kee[int](1)
  ConicalGradient = Kee[int](2)
  NoGradient = Kee[int](3)
