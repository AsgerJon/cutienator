"""
Policy stands for the enum 'QSizePolicy::Policy' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qsizepolicy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Policy(CuteNum):
  """
  The enum 'QSizePolicy::Policy' of Qt, with the 7 names Qt gives in it.
  """

  Fixed = Kee[int](0)
  Minimum = Kee[int](1)
  Maximum = Kee[int](4)
  Preferred = Kee[int](5)
  MinimumExpanding = Kee[int](3)
  Expanding = Kee[int](7)
  Ignored = Kee[int](13)
