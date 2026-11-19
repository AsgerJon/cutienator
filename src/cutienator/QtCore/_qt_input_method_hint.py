"""
InputMethodHint stands for the flags enum 'Qt::InputMethodHint' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class InputMethodHint(CuteFlags, number='unsigned int'):
  """
  The flags enum 'Qt::InputMethodHint' of Qt, with the 25 names Qt gives in
  it. Qt names the type of its combinations 'Qt::InputMethodHints'.
  """

  ImhNone = 0x0
  ImhHiddenText = 0x1
  ImhSensitiveData = 0x2
  ImhNoAutoUppercase = 0x4
  ImhPreferNumbers = 0x8
  ImhPreferUppercase = 0x10
  ImhPreferLowercase = 0x20
  ImhNoPredictiveText = 0x40
  ImhDate = 0x80
  ImhTime = 0x100
  ImhPreferLatin = 0x200
  ImhMultiLine = 0x400
  ImhNoEditMenu = 0x800
  ImhNoTextHandles = 0x1000
  ImhNoFullscreen = 0x2000
  ImhDigitsOnly = 0x10000
  ImhFormattedNumbersOnly = 0x20000
  ImhUppercaseOnly = 0x40000
  ImhLowercaseOnly = 0x80000
  ImhDialableCharactersOnly = 0x100000
  ImhEmailCharactersOnly = 0x200000
  ImhUrlCharactersOnly = 0x400000
  ImhLatinOnly = 0x800000
  ImhDecimalNumbersOnly = 0x1000000
  ImhExclusiveInputMask = 0xffff0000
