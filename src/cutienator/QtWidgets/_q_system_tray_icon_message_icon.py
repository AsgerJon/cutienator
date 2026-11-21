"""
MessageIcon stands for the enum 'QSystemTrayIcon::MessageIcon' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qsystemtrayicon.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MessageIcon(CuteNum):
  """
  The enum 'QSystemTrayIcon::MessageIcon' of Qt, with the 4 names Qt gives in
  it.
  """

  NoIcon = Kee[int](0)
  Information = Kee[int](1)
  Warning = Kee[int](2)
  Critical = Kee[int](3)
