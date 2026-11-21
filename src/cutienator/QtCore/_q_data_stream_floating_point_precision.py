"""
FloatingPointPrecision stands for the enum
'QDataStream::FloatingPointPrecision' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qdatastream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class FloatingPointPrecision(CuteNum):
  """
  The enum 'QDataStream::FloatingPointPrecision' of Qt, with the 2 names Qt
  gives in it.
  """

  SinglePrecision = Kee[int](0)
  DoublePrecision = Kee[int](1)
