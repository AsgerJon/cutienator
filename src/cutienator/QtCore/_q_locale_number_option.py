"""
NumberOption stands for the flags enum 'QLocale::NumberOption' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qlocale.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class NumberOption(CuteFlags):
  """
  The flags enum 'QLocale::NumberOption' of Qt, with the 7 names Qt gives in
  it. Qt names the type of its combinations 'QLocale::NumberOptions'.
  """

  DefaultNumberOptions = 0x0
  OmitGroupSeparator = 0x1
  RejectGroupSeparator = 0x2
  OmitLeadingZeroInExponent = 0x4
  RejectLeadingZeroInExponent = 0x8
  IncludeTrailingZeroesAfterDot = 0x10
  RejectTrailingZeroesAfterDot = 0x20
