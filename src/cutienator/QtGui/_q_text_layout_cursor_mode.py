"""
CursorMode stands for the enum 'QTextLayout::CursorMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class CursorMode(CuteNum):
  """
  The enum 'QTextLayout::CursorMode' of Qt, with the 2 names Qt gives in it.
  """

  SkipCharacters = Kee[int](0)
  SkipWords = Kee[int](1)
