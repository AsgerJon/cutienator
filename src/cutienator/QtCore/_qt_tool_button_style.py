"""
ToolButtonStyle stands for the enum 'Qt::ToolButtonStyle' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ToolButtonStyle(CuteNum):
  """
  The enum 'Qt::ToolButtonStyle' of Qt, with the 5 names Qt gives in it.
  """

  ToolButtonIconOnly = Kee[int](0)
  ToolButtonTextOnly = Kee[int](1)
  ToolButtonTextBesideIcon = Kee[int](2)
  ToolButtonTextUnderIcon = Kee[int](3)
  ToolButtonFollowStyle = Kee[int](4)
