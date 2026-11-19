"""
ComponentFormattingOption stands for the flags enum
'QUrl::ComponentFormattingOption' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qurl.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ComponentFormattingOption(CuteFlags, number='unsigned int'):
  """
  The flags enum 'QUrl::ComponentFormattingOption' of Qt, with the 8 names Qt
  gives in it. Qt names the type of its combinations
  'QUrl::ComponentFormattingOptions'.
  """

  PrettyDecoded = 0x0
  EncodeSpaces = 0x100000
  EncodeUnicode = 0x200000
  EncodeDelimiters = 0xc00000
  EncodeReserved = 0x1000000
  DecodeReserved = 0x2000000
  FullyEncoded = 0x1f00000
  FullyDecoded = 0x7f00000
