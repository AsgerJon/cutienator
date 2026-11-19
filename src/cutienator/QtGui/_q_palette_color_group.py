"""
ColorGroup stands for the enum 'QPalette::ColorGroup' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpalette.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ColorGroup(CuteNum):
  """
  The enum 'QPalette::ColorGroup' of Qt, with the 7 names Qt gives in it.
  """

  Active = Kee[int](0)
  Disabled = Kee[int](1)
  Inactive = Kee[int](2)
  NColorGroups = Kee[int](3)
  Current = Kee[int](4)
  All = Kee[int](5)
  Normal = Kee[int](0)
