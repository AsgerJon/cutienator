"""
MatchFlag stands for the flags enum 'Qt::MatchFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class MatchFlag(CuteFlags):
  """
  The flags enum 'Qt::MatchFlag' of Qt, with the 11 names Qt gives in it. Qt
  names the type of its combinations 'Qt::MatchFlags'.
  """

  MatchExactly = 0x0
  MatchContains = 0x1
  MatchStartsWith = 0x2
  MatchEndsWith = 0x3
  MatchRegularExpression = 0x4
  MatchWildcard = 0x5
  MatchFixedString = 0x8
  MatchTypeMask = 0xf
  MatchCaseSensitive = 0x10
  MatchWrap = 0x20
  MatchRecursive = 0x40
