"""
Flag stands for the flags enum 'QTextOption::Flag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Flag(CuteFlags, number='unsigned int'):
  """
  The flags enum 'QTextOption::Flag' of Qt, with the 8 names Qt gives in it.
  Qt names the type of its combinations 'QTextOption::Flags'.
  """

  ShowTabsAndSpaces = 0x1
  ShowLineAndParagraphSeparators = 0x2
  AddSpaceForLineAndParagraphSeparators = 0x4
  SuppressColors = 0x8
  ShowDocumentTerminator = 0x10
  ShowDefaultIgnorables = 0x20
  DisableEmojiParsing = 0x40
  IncludeTrailingSpaces = 0x80000000
