"""
ToolButtonPopupMode stands for the enum 'QToolButton::ToolButtonPopupMode' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qtoolbutton.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ToolButtonPopupMode(CuteNum):
  """
  The enum 'QToolButton::ToolButtonPopupMode' of Qt, with the 3 names Qt
  gives in it.
  """

  DelayedPopup = Kee[int](0)
  MenuButtonPopup = Kee[int](1)
  InstantPopup = Kee[int](2)
