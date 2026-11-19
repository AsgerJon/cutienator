"""
RegionType stands for the enum 'QRegion::RegionType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qregion.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class RegionType(CuteNum):
  """
  The enum 'QRegion::RegionType' of Qt, with the 2 names Qt gives in it.
  """

  Rectangle = Kee[int](0)
  Ellipse = Kee[int](1)
