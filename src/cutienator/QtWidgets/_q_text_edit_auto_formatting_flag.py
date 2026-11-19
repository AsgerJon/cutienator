"""
AutoFormattingFlag stands for the flags enum 'QTextEdit::AutoFormattingFlag'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qtextedit.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class AutoFormattingFlag(CuteFlags, number='unsigned int'):
  """
  The flags enum 'QTextEdit::AutoFormattingFlag' of Qt, with the 3 names Qt
  gives in it. Qt names the type of its combinations
  'QTextEdit::AutoFormatting'.
  """

  AutoNone = 0x0
  AutoBulletList = 0x1
  AutoAll = 0xffffffff
