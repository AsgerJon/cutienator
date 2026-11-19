"""
FloatingPointPrecisionOption stands for the enum
'QLocale::FloatingPointPrecisionOption' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qlocale.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class FloatingPointPrecisionOption(CuteNum):
  """
  The enum 'QLocale::FloatingPointPrecisionOption' of Qt, with the 1 names Qt
  gives in it.
  """

  FloatingPointShortest = Kee[int](-128)
