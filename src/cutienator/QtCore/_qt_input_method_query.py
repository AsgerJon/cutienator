"""
InputMethodQuery stands for the flags enum 'Qt::InputMethodQuery' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class InputMethodQuery(CuteFlags, number='unsigned int'):
  """
  The flags enum 'Qt::InputMethodQuery' of Qt, with the 20 names Qt gives in
  it. Qt names the type of its combinations 'Qt::InputMethodQueries'.
  """

  ImEnabled = 0x1
  ImCursorRectangle = 0x2
  ImFont = 0x4
  ImCursorPosition = 0x8
  ImSurroundingText = 0x10
  ImCurrentSelection = 0x20
  ImMaximumTextLength = 0x40
  ImAnchorPosition = 0x80
  ImHints = 0x100
  ImPreferredLanguage = 0x200
  ImAbsolutePosition = 0x400
  ImTextBeforeCursor = 0x800
  ImTextAfterCursor = 0x1000
  ImEnterKeyType = 0x2000
  ImAnchorRectangle = 0x4000
  ImInputItemClipRectangle = 0x8000
  ImReadOnly = 0x10000
  ImPlatformData = 0x80000000
  ImQueryInput = 0x40ba
  ImQueryAll = 0xffffffff
