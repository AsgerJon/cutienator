"""
PerformanceHint stands for the enum 'QStaticText::PerformanceHint' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qstatictext.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class PerformanceHint(CuteNum):
  """
  The enum 'QStaticText::PerformanceHint' of Qt, with the 2 names Qt gives in
  it.
  """

  ModerateCaching = Kee[int](0)
  AggressiveCaching = Kee[int](1)
