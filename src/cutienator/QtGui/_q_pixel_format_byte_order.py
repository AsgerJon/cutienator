"""
ByteOrder stands for the enum 'QPixelFormat::ByteOrder' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpixelformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ByteOrder(CuteNum):
  """
  The enum 'QPixelFormat::ByteOrder' of Qt, with the 3 names Qt gives in it.
  """

  LittleEndian = Kee[int](0)
  BigEndian = Kee[int](1)
  CurrentSystemEndian = Kee[int](2)
