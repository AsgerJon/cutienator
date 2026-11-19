"""
NamedColorSpace stands for the enum 'QColorSpace::NamedColorSpace' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qcolorspace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class NamedColorSpace(CuteNum):
  """
  The enum 'QColorSpace::NamedColorSpace' of Qt, with the 8 names Qt gives in
  it.
  """

  SRgb = Kee[int](1)
  SRgbLinear = Kee[int](2)
  AdobeRgb = Kee[int](3)
  DisplayP3 = Kee[int](4)
  ProPhotoRgb = Kee[int](5)
  Bt2020 = Kee[int](6)
  Bt2100Pq = Kee[int](7)
  Bt2100Hlg = Kee[int](8)
