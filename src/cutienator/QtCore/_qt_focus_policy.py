"""
FocusPolicy stands for the enum 'Qt::FocusPolicy' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class FocusPolicy(CuteNum):
  """
  The enum 'Qt::FocusPolicy' of Qt, with the 5 names Qt gives in it.
  """

  NoFocus = Kee[int](0)
  TabFocus = Kee[int](1)
  ClickFocus = Kee[int](2)
  StrongFocus = Kee[int](11)
  WheelFocus = Kee[int](15)
