"""
SizeAdjustPolicy stands for the enum 'QAbstractScrollArea::SizeAdjustPolicy'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qabstractscrollarea.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SizeAdjustPolicy(CuteNum):
  """
  The enum 'QAbstractScrollArea::SizeAdjustPolicy' of Qt, with the 3 names Qt
  gives in it.
  """

  AdjustIgnored = Kee[int](0)
  AdjustToContentsOnFirstShow = Kee[int](1)
  AdjustToContents = Kee[int](2)
