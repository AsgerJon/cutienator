"""
PolicyFlag stands for the enum 'QSizePolicy::PolicyFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qsizepolicy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class PolicyFlag(CuteNum):
  """
  The enum 'QSizePolicy::PolicyFlag' of Qt, with the 4 names Qt gives in it.
  """

  GrowFlag = Kee[int](1)
  ExpandFlag = Kee[int](2)
  ShrinkFlag = Kee[int](4)
  IgnoreFlag = Kee[int](8)
