"""
Section stands for the flags enum 'QDateTimeEdit::Section' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qdatetimeedit.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class Section(CuteFlags):
  """
  The flags enum 'QDateTimeEdit::Section' of Qt, with the 11 names Qt gives
  in it. Qt names the type of its combinations 'QDateTimeEdit::Sections'.
  """

  NoSection = 0x0
  AmPmSection = 0x1
  MSecSection = 0x2
  SecondSection = 0x4
  MinuteSection = 0x8
  HourSection = 0x10
  DaySection = 0x100
  MonthSection = 0x200
  YearSection = 0x400
  TimeSections_Mask = 0x1f
  DateSections_Mask = 0x700
