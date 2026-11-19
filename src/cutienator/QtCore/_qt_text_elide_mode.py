"""
TextElideMode stands for the enum 'Qt::TextElideMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TextElideMode(CuteNum):
  """
  The enum 'Qt::TextElideMode' of Qt, with the 4 names Qt gives in it.
  """

  ElideLeft = Kee[int](0)
  ElideRight = Kee[int](1)
  ElideMiddle = Kee[int](2)
  ElideNone = Kee[int](3)
