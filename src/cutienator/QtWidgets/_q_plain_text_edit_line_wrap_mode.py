"""
LineWrapMode stands for the enum 'QPlainTextEdit::LineWrapMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qplaintextedit.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class LineWrapMode(CuteNum):
  """
  The enum 'QPlainTextEdit::LineWrapMode' of Qt, with the 2 names Qt gives in
  it.
  """

  NoWrap = Kee[int](0)
  WidgetWidth = Kee[int](1)
