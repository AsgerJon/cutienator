"""
MoveMode stands for the enum 'QTextCursor::MoveMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextcursor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MoveMode(CuteNum):
  """
  The enum 'QTextCursor::MoveMode' of Qt, with the 2 names Qt gives in it.
  """

  MoveAnchor = Kee[int](0)
  KeepAnchor = Kee[int](1)
