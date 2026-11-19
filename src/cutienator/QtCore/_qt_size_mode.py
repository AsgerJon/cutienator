"""
SizeMode stands for the enum 'Qt::SizeMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SizeMode(CuteNum):
  """
  The enum 'Qt::SizeMode' of Qt, with the 2 names Qt gives in it.
  """

  AbsoluteSize = Kee[int](0)
  RelativeSize = Kee[int](1)
