"""
ObjectTypes stands for the enum 'QTextFormat::ObjectTypes' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ObjectTypes(CuteNum):
  """
  The enum 'QTextFormat::ObjectTypes' of Qt, with the 5 names Qt gives in it.
  """

  NoObject = Kee[int](0)
  ImageObject = Kee[int](1)
  TableObject = Kee[int](2)
  TableCellObject = Kee[int](3)
  UserObject = Kee[int](4096)
