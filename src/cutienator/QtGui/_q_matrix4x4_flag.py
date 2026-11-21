"""
Flag stands for the flags enum 'QMatrix4x4::Flag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qmatrix4x4.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Flag(CuteFlags):
  """
  The flags enum 'QMatrix4x4::Flag' of Qt, with the 7 names Qt gives in it.
  Qt names the type of its combinations 'QMatrix4x4::Flags'.
  """

  Identity = 0x0
  Translation = 0x1
  Scale = 0x2
  Rotation2D = 0x4
  Rotation = 0x8
  Perspective = 0x10
  General = 0x1f
