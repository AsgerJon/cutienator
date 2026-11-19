"""
MaskMode stands for the enum 'Qt::MaskMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MaskMode(CuteNum):
  """
  The enum 'Qt::MaskMode' of Qt, with the 2 names Qt gives in it.
  """

  MaskInColor = Kee[int](0)
  MaskOutColor = Kee[int](1)
