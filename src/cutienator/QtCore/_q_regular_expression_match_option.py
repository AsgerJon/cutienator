"""
MatchOption stands for the flags enum 'QRegularExpression::MatchOption' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qregularexpression.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class MatchOption(CuteFlags):
  """
  The flags enum 'QRegularExpression::MatchOption' of Qt, with the 4 names Qt
  gives in it. Qt names the type of its combinations
  'QRegularExpression::MatchOptions'.
  """

  NoMatchOption = 0x0
  AnchorAtOffsetMatchOption = 0x1
  AnchoredMatchOption = 0x1
  DontCheckSubjectStringMatchOption = 0x2
