"""
RealNumberNotation stands for the enum 'QTextStream::RealNumberNotation' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qtextstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class RealNumberNotation(CuteNum):
  """
  The enum 'QTextStream::RealNumberNotation' of Qt, with the 3 names Qt gives
  in it.
  """

  SmartNotation = Kee[int](0)
  FixedNotation = Kee[int](1)
  ScientificNotation = Kee[int](2)
