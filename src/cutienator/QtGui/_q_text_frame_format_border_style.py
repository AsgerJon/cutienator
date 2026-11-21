"""
BorderStyle stands for the enum 'QTextFrameFormat::BorderStyle' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class BorderStyle(CuteNum):
  """
  The enum 'QTextFrameFormat::BorderStyle' of Qt, with the 11 names Qt gives
  in it.
  """

  BorderStyle_None = Kee[int](0)
  BorderStyle_Dotted = Kee[int](1)
  BorderStyle_Dashed = Kee[int](2)
  BorderStyle_Solid = Kee[int](3)
  BorderStyle_Double = Kee[int](4)
  BorderStyle_DotDash = Kee[int](5)
  BorderStyle_DotDotDash = Kee[int](6)
  BorderStyle_Groove = Kee[int](7)
  BorderStyle_Ridge = Kee[int](8)
  BorderStyle_Inset = Kee[int](9)
  BorderStyle_Outset = Kee[int](10)
