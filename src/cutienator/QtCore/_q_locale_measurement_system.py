"""
MeasurementSystem stands for the enum 'QLocale::MeasurementSystem' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qlocale.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MeasurementSystem(CuteNum):
  """
  The enum 'QLocale::MeasurementSystem' of Qt, with the 4 names Qt gives in
  it.
  """

  MetricSystem = Kee[int](0)
  ImperialUSSystem = Kee[int](1)
  ImperialUKSystem = Kee[int](2)
  ImperialSystem = Kee[int](1)
