"""
MoveOperation stands for the enum 'QTextCursor::MoveOperation' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextcursor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MoveOperation(CuteNum):
  """
  The enum 'QTextCursor::MoveOperation' of Qt, with the 25 names Qt gives in
  it.
  """

  NoMove = Kee[int](0)
  Start = Kee[int](1)
  Up = Kee[int](2)
  StartOfLine = Kee[int](3)
  StartOfBlock = Kee[int](4)
  StartOfWord = Kee[int](5)
  PreviousBlock = Kee[int](6)
  PreviousCharacter = Kee[int](7)
  PreviousWord = Kee[int](8)
  Left = Kee[int](9)
  WordLeft = Kee[int](10)
  End = Kee[int](11)
  Down = Kee[int](12)
  EndOfLine = Kee[int](13)
  EndOfWord = Kee[int](14)
  EndOfBlock = Kee[int](15)
  NextBlock = Kee[int](16)
  NextCharacter = Kee[int](17)
  NextWord = Kee[int](18)
  Right = Kee[int](19)
  WordRight = Kee[int](20)
  NextCell = Kee[int](21)
  PreviousCell = Kee[int](22)
  NextRow = Kee[int](23)
  PreviousRow = Kee[int](24)
