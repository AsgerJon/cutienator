"""
TypeInterpretation stands for the enum 'QPixelFormat::TypeInterpretation' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpixelformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TypeInterpretation(CuteNum):
  """
  The enum 'QPixelFormat::TypeInterpretation' of Qt, with the 4 names Qt
  gives in it.
  """

  UnsignedInteger = Kee[int](0)
  UnsignedShort = Kee[int](1)
  UnsignedByte = Kee[int](2)
  FloatingPoint = Kee[int](3)
