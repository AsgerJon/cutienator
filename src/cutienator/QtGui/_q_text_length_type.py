"""
Type stands for the enum 'QTextLength::Type' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Type(CuteNum):
  """
  The enum 'QTextLength::Type' of Qt, with the 3 names Qt gives in it.
  """

  VariableLength = Kee[int](0)
  FixedLength = Kee[int](1)
  PercentageLength = Kee[int](2)
