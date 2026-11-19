"""
FieldGrowthPolicy stands for the enum 'QFormLayout::FieldGrowthPolicy' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qformlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class FieldGrowthPolicy(CuteNum):
  """
  The enum 'QFormLayout::FieldGrowthPolicy' of Qt, with the 3 names Qt gives
  in it.
  """

  FieldsStayAtSizeHint = Kee[int](0)
  ExpandingFieldsGrow = Kee[int](1)
  AllNonFixedFieldsGrow = Kee[int](2)
