"""
Primaries stands for the enum 'QColorSpace::Primaries' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qcolorspace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Primaries(CuteNum, scoped=True):
  """
  The enum 'QColorSpace::Primaries' of Qt, with the 6 names Qt gives in it.
  C++ keeps these names inside the enum, so the class that holds the enum
  does not have them.
  """

  Custom = Kee[int](0)
  SRgb = Kee[int](1)
  AdobeRgb = Kee[int](2)
  DciP3D65 = Kee[int](3)
  ProPhotoRgb = Kee[int](4)
  Bt2020 = Kee[int](5)
