"""
CorrectionMode stands for the enum 'QAbstractSpinBox::CorrectionMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qabstractspinbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class CorrectionMode(CuteNum):
  """
  The enum 'QAbstractSpinBox::CorrectionMode' of Qt, with the 2 names Qt
  gives in it.
  """

  CorrectToPreviousValue = Kee[int](0)
  CorrectToNearestValue = Kee[int](1)
