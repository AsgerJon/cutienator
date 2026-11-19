"""
WildcardConversionOption stands for the flags enum
'QRegularExpression::WildcardConversionOption' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qregularexpression.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class WildcardConversionOption(CuteFlags):
  """
  The flags enum 'QRegularExpression::WildcardConversionOption' of Qt, with
  the 3 names Qt gives in it. Qt names the type of its combinations
  'QRegularExpression::WildcardConversionOptions'.
  """

  DefaultWildcardConversion = 0x0
  UnanchoredWildcardConversion = 0x1
  NonPathWildcardConversion = 0x2
