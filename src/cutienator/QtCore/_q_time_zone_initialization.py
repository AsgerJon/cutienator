"""
Initialization stands for the enum 'QTimeZone::Initialization' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qtimezone.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Initialization(CuteNum):
  """
  The enum 'QTimeZone::Initialization' of Qt, with the 2 names Qt gives in
  it.
  """

  LocalTime = Kee[int](0)
  UTC = Kee[int](1)
