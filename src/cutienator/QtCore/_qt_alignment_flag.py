"""
AlignmentFlag stands for the flags enum 'Qt::AlignmentFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class AlignmentFlag(CuteFlags):
  """
  The flags enum 'Qt::AlignmentFlag' of Qt, with the 14 names Qt gives in it.
  Qt names the type of its combinations 'Qt::Alignment'.
  """

  AlignLeft = 0x1
  AlignLeading = 0x1
  AlignRight = 0x2
  AlignTrailing = 0x2
  AlignHCenter = 0x4
  AlignJustify = 0x8
  AlignAbsolute = 0x10
  AlignHorizontal_Mask = 0x1f
  AlignTop = 0x20
  AlignBottom = 0x40
  AlignVCenter = 0x80
  AlignBaseline = 0x100
  AlignVertical_Mask = 0x1e0
  AlignCenter = 0x84
