"""
Stacks stands for the enum 'QTextDocument::Stacks' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextdocument.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Stacks(CuteNum):
  """
  The enum 'QTextDocument::Stacks' of Qt, with the 3 names Qt gives in it.
  """

  UndoStack = Kee[int](1)
  RedoStack = Kee[int](2)
  UndoAndRedoStacks = Kee[int](3)
