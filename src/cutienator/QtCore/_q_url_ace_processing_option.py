"""
AceProcessingOption stands for the flags enum 'QUrl::AceProcessingOption' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qurl.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class AceProcessingOption(CuteFlags, number='unsigned int'):
  """
  The flags enum 'QUrl::AceProcessingOption' of Qt, with the 2 names Qt gives
  in it. Qt names the type of its combinations 'QUrl::AceProcessingOptions'.
  """

  IgnoreIDNWhitelist = 0x1
  AceTransitionalProcessing = 0x2
