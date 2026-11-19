"""
PatternOption stands for the flags enum 'QRegularExpression::PatternOption'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qregularexpression.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class PatternOption(CuteFlags):
  """
  The flags enum 'QRegularExpression::PatternOption' of Qt, with the 8 names
  Qt gives in it. Qt names the type of its combinations
  'QRegularExpression::PatternOptions'.
  """

  NoPatternOption = 0x0
  CaseInsensitiveOption = 0x1
  DotMatchesEverythingOption = 0x2
  MultilineOption = 0x4
  ExtendedPatternSyntaxOption = 0x8
  InvertedGreedinessOption = 0x10
  DontCaptureOption = 0x20
  UseUnicodePropertiesOption = 0x40
