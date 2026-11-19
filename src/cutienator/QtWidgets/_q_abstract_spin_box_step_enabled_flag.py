"""
StepEnabledFlag stands for the flags enum 'QAbstractSpinBox::StepEnabledFlag'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qabstractspinbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class StepEnabledFlag(CuteFlags):
  """
  The flags enum 'QAbstractSpinBox::StepEnabledFlag' of Qt, with the 3 names
  Qt gives in it. Qt names the type of its combinations
  'QAbstractSpinBox::StepEnabled'.
  """

  StepNone = 0x0
  StepUpEnabled = 0x1
  StepDownEnabled = 0x2
