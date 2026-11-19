"""
LineHeightTypes stands for the enum 'QTextBlockFormat::LineHeightTypes' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class LineHeightTypes(CuteNum):
  """
  The enum 'QTextBlockFormat::LineHeightTypes' of Qt, with the 5 names Qt
  gives in it.
  """

  SingleHeight = Kee[int](0)
  ProportionalHeight = Kee[int](1)
  FixedHeight = Kee[int](2)
  MinimumHeight = Kee[int](3)
  LineDistanceHeight = Kee[int](4)
