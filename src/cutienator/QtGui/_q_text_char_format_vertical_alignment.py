"""
VerticalAlignment stands for the enum 'QTextCharFormat::VerticalAlignment' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class VerticalAlignment(CuteNum):
  """
  The enum 'QTextCharFormat::VerticalAlignment' of Qt, with the 7 names Qt
  gives in it.
  """

  AlignNormal = Kee[int](0)
  AlignSuperScript = Kee[int](1)
  AlignSubScript = Kee[int](2)
  AlignMiddle = Kee[int](3)
  AlignTop = Kee[int](4)
  AlignBottom = Kee[int](5)
  AlignBaseline = Kee[int](6)
