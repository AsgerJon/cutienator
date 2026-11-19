"""
TextFormat stands for the enum 'Qt::TextFormat' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TextFormat(CuteNum):
  """
  The enum 'Qt::TextFormat' of Qt, with the 4 names Qt gives in it.
  """

  PlainText = Kee[int](0)
  RichText = Kee[int](1)
  AutoText = Kee[int](2)
  MarkdownText = Kee[int](3)
