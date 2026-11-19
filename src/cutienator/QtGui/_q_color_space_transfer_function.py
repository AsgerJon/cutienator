"""
TransferFunction stands for the enum 'QColorSpace::TransferFunction' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qcolorspace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TransferFunction(CuteNum, scoped=True):
  """
  The enum 'QColorSpace::TransferFunction' of Qt, with the 8 names Qt gives
  in it. C++ keeps these names inside the enum, so the class that holds the
  enum does not have them.
  """

  Custom = Kee[int](0)
  Linear = Kee[int](1)
  Gamma = Kee[int](2)
  SRgb = Kee[int](3)
  ProPhotoRgb = Kee[int](4)
  Bt2020 = Kee[int](5)
  St2084 = Kee[int](6)
  Hlg = Kee[int](7)
