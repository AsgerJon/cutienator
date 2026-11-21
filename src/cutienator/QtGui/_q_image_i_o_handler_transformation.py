"""
Transformation stands for the flags enum 'QImageIOHandler::Transformation' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qimageiohandler.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Transformation(CuteFlags):
  """
  The flags enum 'QImageIOHandler::Transformation' of Qt, with the 8 names Qt
  gives in it. Qt names the type of its combinations
  'QImageIOHandler::Transformations'.
  """

  TransformationNone = 0x0
  TransformationMirror = 0x1
  TransformationFlip = 0x2
  TransformationRotate180 = 0x3
  TransformationRotate90 = 0x4
  TransformationMirrorAndRotate90 = 0x5
  TransformationFlipAndRotate90 = 0x6
  TransformationRotate270 = 0x7
