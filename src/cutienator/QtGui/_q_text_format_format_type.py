"""
FormatType stands for the enum 'QTextFormat::FormatType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class FormatType(CuteNum):
  """
  The enum 'QTextFormat::FormatType' of Qt, with the 6 names Qt gives in it.
  """

  InvalidFormat = Kee[int](-1)
  BlockFormat = Kee[int](1)
  CharFormat = Kee[int](2)
  ListFormat = Kee[int](3)
  FrameFormat = Kee[int](5)
  UserFormat = Kee[int](100)
