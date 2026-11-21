"""
ChangeFlag stands for the flags enum 'QPinchGesture::ChangeFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ChangeFlag(CuteFlags):
  """
  The flags enum 'QPinchGesture::ChangeFlag' of Qt, with the 3 names Qt gives
  in it. Qt names the type of its combinations 'QPinchGesture::ChangeFlags'.
  """

  ScaleFactorChanged = 0x1
  RotationAngleChanged = 0x2
  CenterPointChanged = 0x4
