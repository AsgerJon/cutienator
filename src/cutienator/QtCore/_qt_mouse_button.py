"""
MouseButton stands for the flags enum 'Qt::MouseButton' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class MouseButton(CuteFlags, number='unsigned int'):
  """
  The flags enum 'Qt::MouseButton' of Qt, with the 36 names Qt gives in it.
  Qt names the type of its combinations 'Qt::MouseButtons'.
  """

  NoButton = 0x0
  LeftButton = 0x1
  RightButton = 0x2
  MiddleButton = 0x4
  BackButton = 0x8
  XButton1 = 0x8
  ExtraButton1 = 0x8
  ForwardButton = 0x10
  XButton2 = 0x10
  ExtraButton2 = 0x10
  TaskButton = 0x20
  ExtraButton3 = 0x20
  ExtraButton4 = 0x40
  ExtraButton5 = 0x80
  ExtraButton6 = 0x100
  ExtraButton7 = 0x200
  ExtraButton8 = 0x400
  ExtraButton9 = 0x800
  ExtraButton10 = 0x1000
  ExtraButton11 = 0x2000
  ExtraButton12 = 0x4000
  ExtraButton13 = 0x8000
  ExtraButton14 = 0x10000
  ExtraButton15 = 0x20000
  ExtraButton16 = 0x40000
  ExtraButton17 = 0x80000
  ExtraButton18 = 0x100000
  ExtraButton19 = 0x200000
  ExtraButton20 = 0x400000
  ExtraButton21 = 0x800000
  ExtraButton22 = 0x1000000
  ExtraButton23 = 0x2000000
  ExtraButton24 = 0x4000000
  AllButtons = 0x7ffffff
  MaxMouseButton = 0x4000000
  MouseButtonMask = 0xffffffff
