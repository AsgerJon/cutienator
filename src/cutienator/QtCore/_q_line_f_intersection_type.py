"""
IntersectionType stands for the enum 'QLineF::IntersectionType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qline.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class IntersectionType(CuteNum):
  """
  The enum 'QLineF::IntersectionType' of Qt, with the 3 names Qt gives in it.
  """

  NoIntersection = Kee[int](0)
  BoundedIntersection = Kee[int](1)
  UnboundedIntersection = Kee[int](2)
