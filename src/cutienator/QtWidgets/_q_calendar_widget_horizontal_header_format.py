"""
HorizontalHeaderFormat stands for the enum
'QCalendarWidget::HorizontalHeaderFormat' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qcalendarwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class HorizontalHeaderFormat(CuteNum):
  """
  The enum 'QCalendarWidget::HorizontalHeaderFormat' of Qt, with the 4 names
  Qt gives in it.
  """

  NoHorizontalHeader = Kee[int](0)
  SingleLetterDayNames = Kee[int](1)
  ShortDayNames = Kee[int](2)
  LongDayNames = Kee[int](3)
