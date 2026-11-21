"""
Status stands for the enum 'QTextStream::Status' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qtextstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Status(CuteNum):
  """
  The enum 'QTextStream::Status' of Qt, with the 4 names Qt gives in it.
  """

  Ok = Kee[int](0)
  ReadPastEnd = Kee[int](1)
  ReadCorruptData = Kee[int](2)
  WriteFailed = Kee[int](3)
