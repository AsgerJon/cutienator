"""
TextInteractionFlag stands for the flags enum 'Qt::TextInteractionFlag' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class TextInteractionFlag(CuteFlags):
  """
  The flags enum 'Qt::TextInteractionFlag' of Qt, with the 8 names Qt gives
  in it. Qt names the type of its combinations 'Qt::TextInteractionFlags'.
  """

  NoTextInteraction = 0x0
  TextSelectableByMouse = 0x1
  TextSelectableByKeyboard = 0x2
  LinksAccessibleByMouse = 0x4
  LinksAccessibleByKeyboard = 0x8
  TextEditable = 0x10
  TextEditorInteraction = 0x13
  TextBrowserInteraction = 0xd
