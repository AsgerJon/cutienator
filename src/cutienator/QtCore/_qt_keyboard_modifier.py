"""
KeyboardModifier stands for the flags enum 'Qt::KeyboardModifier' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class KeyboardModifier(CuteFlags, number='unsigned int'):
  """
  The flags enum 'Qt::KeyboardModifier' of Qt, with the 8 names Qt gives in
  it. Qt names the type of its combinations 'Qt::KeyboardModifiers'.
  """

  NoModifier = 0x0
  ShiftModifier = 0x2000000
  ControlModifier = 0x4000000
  AltModifier = 0x8000000
  MetaModifier = 0x10000000
  KeypadModifier = 0x20000000
  GroupSwitchModifier = 0x40000000
  KeyboardModifierMask = 0xfe000000
