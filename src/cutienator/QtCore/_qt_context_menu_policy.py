"""
ContextMenuPolicy stands for the enum 'Qt::ContextMenuPolicy' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ContextMenuPolicy(CuteNum):
  """
  The enum 'Qt::ContextMenuPolicy' of Qt, with the 5 names Qt gives in it.
  """

  NoContextMenu = Kee[int](0)
  DefaultContextMenu = Kee[int](1)
  ActionsContextMenu = Kee[int](2)
  CustomContextMenu = Kee[int](3)
  PreventContextMenu = Kee[int](4)
