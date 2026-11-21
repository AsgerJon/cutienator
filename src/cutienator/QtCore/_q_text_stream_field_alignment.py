"""
FieldAlignment stands for the enum 'QTextStream::FieldAlignment' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qtextstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class FieldAlignment(CuteNum):
  """
  The enum 'QTextStream::FieldAlignment' of Qt, with the 4 names Qt gives in
  it.
  """

  AlignLeft = Kee[int](0)
  AlignRight = Kee[int](1)
  AlignCenter = Kee[int](2)
  AlignAccountingStyle = Kee[int](3)
