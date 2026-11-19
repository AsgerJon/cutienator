"""
StandardKey stands for the enum 'QKeySequence::StandardKey' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qkeysequence.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class StandardKey(CuteNum):
  """
  The enum 'QKeySequence::StandardKey' of Qt, with the 71 names Qt gives in
  it.
  """

  UnknownKey = Kee[int](0)
  HelpContents = Kee[int](1)
  WhatsThis = Kee[int](2)
  Open = Kee[int](3)
  Close = Kee[int](4)
  Save = Kee[int](5)
  New = Kee[int](6)
  Delete = Kee[int](7)
  Cut = Kee[int](8)
  Copy = Kee[int](9)
  Paste = Kee[int](10)
  Undo = Kee[int](11)
  Redo = Kee[int](12)
  Back = Kee[int](13)
  Forward = Kee[int](14)
  Refresh = Kee[int](15)
  ZoomIn = Kee[int](16)
  ZoomOut = Kee[int](17)
  Print = Kee[int](18)
  AddTab = Kee[int](19)
  NextChild = Kee[int](20)
  PreviousChild = Kee[int](21)
  Find = Kee[int](22)
  FindNext = Kee[int](23)
  FindPrevious = Kee[int](24)
  Replace = Kee[int](25)
  SelectAll = Kee[int](26)
  Bold = Kee[int](27)
  Italic = Kee[int](28)
  Underline = Kee[int](29)
  MoveToNextChar = Kee[int](30)
  MoveToPreviousChar = Kee[int](31)
  MoveToNextWord = Kee[int](32)
  MoveToPreviousWord = Kee[int](33)
  MoveToNextLine = Kee[int](34)
  MoveToPreviousLine = Kee[int](35)
  MoveToNextPage = Kee[int](36)
  MoveToPreviousPage = Kee[int](37)
  MoveToStartOfLine = Kee[int](38)
  MoveToEndOfLine = Kee[int](39)
  MoveToStartOfBlock = Kee[int](40)
  MoveToEndOfBlock = Kee[int](41)
  MoveToStartOfDocument = Kee[int](42)
  MoveToEndOfDocument = Kee[int](43)
  SelectNextChar = Kee[int](44)
  SelectPreviousChar = Kee[int](45)
  SelectNextWord = Kee[int](46)
  SelectPreviousWord = Kee[int](47)
  SelectNextLine = Kee[int](48)
  SelectPreviousLine = Kee[int](49)
  SelectNextPage = Kee[int](50)
  SelectPreviousPage = Kee[int](51)
  SelectStartOfLine = Kee[int](52)
  SelectEndOfLine = Kee[int](53)
  SelectStartOfBlock = Kee[int](54)
  SelectEndOfBlock = Kee[int](55)
  SelectStartOfDocument = Kee[int](56)
  SelectEndOfDocument = Kee[int](57)
  DeleteStartOfWord = Kee[int](58)
  DeleteEndOfWord = Kee[int](59)
  DeleteEndOfLine = Kee[int](60)
  InsertParagraphSeparator = Kee[int](61)
  InsertLineSeparator = Kee[int](62)
  SaveAs = Kee[int](63)
  Preferences = Kee[int](64)
  Quit = Kee[int](65)
  FullScreen = Kee[int](66)
  Deselect = Kee[int](67)
  DeleteCompleteLine = Kee[int](68)
  Backspace = Kee[int](69)
  Cancel = Kee[int](70)
