"""
TransformationType stands for the enum 'QTransform::TransformationType' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtransform.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TransformationType(CuteNum):
  """
  The enum 'QTransform::TransformationType' of Qt, with the 6 names Qt gives
  in it.
  """

  TxNone = Kee[int](0)
  TxTranslate = Kee[int](1)
  TxScale = Kee[int](2)
  TxRotate = Kee[int](4)
  TxShear = Kee[int](8)
  TxProject = Kee[int](16)
