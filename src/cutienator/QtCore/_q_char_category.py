"""
Category stands for the enum 'QChar::Category' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/qchar.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Category(CuteNum):
  """
  The enum 'QChar::Category' of Qt, with the 30 names Qt gives in it.
  """

  Mark_NonSpacing = Kee[int](0)
  Mark_SpacingCombining = Kee[int](1)
  Mark_Enclosing = Kee[int](2)
  Number_DecimalDigit = Kee[int](3)
  Number_Letter = Kee[int](4)
  Number_Other = Kee[int](5)
  Separator_Space = Kee[int](6)
  Separator_Line = Kee[int](7)
  Separator_Paragraph = Kee[int](8)
  Other_Control = Kee[int](9)
  Other_Format = Kee[int](10)
  Other_Surrogate = Kee[int](11)
  Other_PrivateUse = Kee[int](12)
  Other_NotAssigned = Kee[int](13)
  Letter_Uppercase = Kee[int](14)
  Letter_Lowercase = Kee[int](15)
  Letter_Titlecase = Kee[int](16)
  Letter_Modifier = Kee[int](17)
  Letter_Other = Kee[int](18)
  Punctuation_Connector = Kee[int](19)
  Punctuation_Dash = Kee[int](20)
  Punctuation_Open = Kee[int](21)
  Punctuation_Close = Kee[int](22)
  Punctuation_InitialQuote = Kee[int](23)
  Punctuation_FinalQuote = Kee[int](24)
  Punctuation_Other = Kee[int](25)
  Symbol_Math = Kee[int](26)
  Symbol_Currency = Kee[int](27)
  Symbol_Modifier = Kee[int](28)
  Symbol_Other = Kee[int](29)
