"""
LanguageCodeType stands for the flags enum 'QLocale::LanguageCodeType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qlocale.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class LanguageCodeType(CuteFlags):
  """
  The flags enum 'QLocale::LanguageCodeType' of Qt, with the 10 names Qt
  gives in it. Qt names the type of its combinations
  'QLocale::LanguageCodeTypes'.
  """

  ISO639Part1 = 0x1
  ISO639Part2B = 0x2
  ISO639Part2T = 0x4
  ISO639Part3 = 0x8
  LegacyLanguageCode = 0x8000
  ISO639Part2 = 0x6
  ISO639Alpha2 = 0x1
  ISO639Alpha3 = 0xe
  ISO639 = 0xf
  AnyLanguageCode = -1
