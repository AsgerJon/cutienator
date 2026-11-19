"""
ActionEvent stands for the enum 'QAction::ActionEvent' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qaction.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ActionEvent(CuteNum):
  """
  The enum 'QAction::ActionEvent' of Qt, with the 2 names Qt gives in it.
  """

  Trigger = Kee[int](0)
  Hover = Kee[int](1)
