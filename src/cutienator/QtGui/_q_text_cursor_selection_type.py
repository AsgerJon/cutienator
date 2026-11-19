"""
SelectionType stands for the enum 'QTextCursor::SelectionType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextcursor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class SelectionType(CuteNum):
  """
  The enum 'QTextCursor::SelectionType' of Qt, with the 4 names Qt gives in
  it.
  """

  WordUnderCursor = Kee[int](0)
  LineUnderCursor = Kee[int](1)
  BlockUnderCursor = Kee[int](2)
  Document = Kee[int](3)
