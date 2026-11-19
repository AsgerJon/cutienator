"""
TextFlag stands for the enum 'Qt::TextFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TextFlag(CuteNum):
  """
  The enum 'Qt::TextFlag' of Qt, with the 13 names Qt gives in it.
  """

  TextSingleLine = Kee[int](256)
  TextDontClip = Kee[int](512)
  TextExpandTabs = Kee[int](1024)
  TextShowMnemonic = Kee[int](2048)
  TextWordWrap = Kee[int](4096)
  TextWrapAnywhere = Kee[int](8192)
  TextDontPrint = Kee[int](16384)
  TextIncludeTrailingSpaces = Kee[int](134217728)
  TextHideMnemonic = Kee[int](32768)
  TextJustificationForced = Kee[int](65536)
  TextForceLeftToRight = Kee[int](131072)
  TextForceRightToLeft = Kee[int](262144)
  TextLongestVariant = Kee[int](524288)
