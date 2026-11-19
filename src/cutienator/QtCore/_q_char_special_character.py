"""
SpecialCharacter stands for the enum 'QChar::SpecialCharacter' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qchar.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SpecialCharacter(CuteNum):
  """
  The enum 'QChar::SpecialCharacter' of Qt, with the 16 names Qt gives in it.
  """

  Null = Kee[int](0)
  Tabulation = Kee[int](9)
  LineFeed = Kee[int](10)
  FormFeed = Kee[int](12)
  CarriageReturn = Kee[int](13)
  Space = Kee[int](32)
  Nbsp = Kee[int](160)
  SoftHyphen = Kee[int](173)
  ReplacementCharacter = Kee[int](65533)
  ObjectReplacementCharacter = Kee[int](65532)
  ByteOrderMark = Kee[int](65279)
  ByteOrderSwapped = Kee[int](65534)
  ParagraphSeparator = Kee[int](8233)
  LineSeparator = Kee[int](8232)
  VisualTabCharacter = Kee[int](8594)
  LastValidCodePoint = Kee[int](1114111)
