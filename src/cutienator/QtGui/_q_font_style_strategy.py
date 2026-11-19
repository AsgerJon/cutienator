"""
StyleStrategy stands for the enum 'QFont::StyleStrategy' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qfont.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class StyleStrategy(CuteNum):
  """
  The enum 'QFont::StyleStrategy' of Qt, with the 14 names Qt gives in it.
  """

  PreferDefault = Kee[int](1)
  PreferBitmap = Kee[int](2)
  PreferDevice = Kee[int](4)
  PreferOutline = Kee[int](8)
  ForceOutline = Kee[int](16)
  PreferMatch = Kee[int](32)
  PreferQuality = Kee[int](64)
  PreferAntialias = Kee[int](128)
  NoAntialias = Kee[int](256)
  NoSubpixelAntialias = Kee[int](2048)
  PreferNoShaping = Kee[int](4096)
  ContextFontMerging = Kee[int](8192)
  PreferTypoLineMetrics = Kee[int](16384)
  NoFontMerging = Kee[int](32768)
