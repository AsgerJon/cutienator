"""
MatchType stands for the enum 'QRegularExpression::MatchType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qregularexpression.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MatchType(CuteNum):
  """
  The enum 'QRegularExpression::MatchType' of Qt, with the 4 names Qt gives
  in it.
  """

  NormalMatch = Kee[int](0)
  PartialPreferCompleteMatch = Kee[int](1)
  PartialPreferFirstMatch = Kee[int](2)
  NoMatch = Kee[int](3)
