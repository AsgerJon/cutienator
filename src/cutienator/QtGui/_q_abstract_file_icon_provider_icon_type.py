"""
IconType stands for the enum 'QAbstractFileIconProvider::IconType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qabstractfileiconprovider.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class IconType(CuteNum):
  """
  The enum 'QAbstractFileIconProvider::IconType' of Qt, with the 7 names Qt
  gives in it.
  """

  Computer = Kee[int](0)
  Desktop = Kee[int](1)
  Trashcan = Kee[int](2)
  Network = Kee[int](3)
  Drive = Kee[int](4)
  Folder = Kee[int](5)
  File = Kee[int](6)
