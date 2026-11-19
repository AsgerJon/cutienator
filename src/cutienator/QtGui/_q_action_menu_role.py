"""
MenuRole stands for the enum 'QAction::MenuRole' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qaction.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MenuRole(CuteNum):
  """
  The enum 'QAction::MenuRole' of Qt, with the 7 names Qt gives in it.
  """

  NoRole = Kee[int](0)
  TextHeuristicRole = Kee[int](1)
  ApplicationSpecificRole = Kee[int](2)
  AboutQtRole = Kee[int](3)
  AboutRole = Kee[int](4)
  PreferencesRole = Kee[int](5)
  QuitRole = Kee[int](6)
