"""
FontFilter stands for the flags enum 'QFontComboBox::FontFilter' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qfontcombobox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class FontFilter(CuteFlags):
  """
  The flags enum 'QFontComboBox::FontFilter' of Qt, with the 5 names Qt gives
  in it. Qt names the type of its combinations 'QFontComboBox::FontFilters'.
  """

  AllFonts = 0x0
  ScalableFonts = 0x1
  NonScalableFonts = 0x2
  MonospacedFonts = 0x4
  ProportionalFonts = 0x8
