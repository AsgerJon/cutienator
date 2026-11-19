"""
SizeMatchPolicy stands for the enum 'QPageSize::SizeMatchPolicy' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpagesize.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SizeMatchPolicy(CuteNum):
  """
  The enum 'QPageSize::SizeMatchPolicy' of Qt, with the 3 names Qt gives in
  it.
  """

  FuzzyMatch = Kee[int](0)
  FuzzyOrientationMatch = Kee[int](1)
  ExactMatch = Kee[int](2)
