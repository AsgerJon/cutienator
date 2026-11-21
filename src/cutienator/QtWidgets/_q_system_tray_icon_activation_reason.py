"""
ActivationReason stands for the enum 'QSystemTrayIcon::ActivationReason' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qsystemtrayicon.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ActivationReason(CuteNum):
  """
  The enum 'QSystemTrayIcon::ActivationReason' of Qt, with the 5 names Qt
  gives in it.
  """

  Unknown = Kee[int](0)
  Context = Kee[int](1)
  DoubleClick = Kee[int](2)
  Trigger = Kee[int](3)
  MiddleClick = Kee[int](4)
