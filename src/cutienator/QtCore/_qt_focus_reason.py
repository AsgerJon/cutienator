"""
FocusReason stands for the enum 'Qt::FocusReason' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class FocusReason(CuteNum):
  """
  The enum 'Qt::FocusReason' of Qt, with the 9 names Qt gives in it.
  """

  MouseFocusReason = Kee[int](0)
  TabFocusReason = Kee[int](1)
  BacktabFocusReason = Kee[int](2)
  ActiveWindowFocusReason = Kee[int](3)
  PopupFocusReason = Kee[int](4)
  ShortcutFocusReason = Kee[int](5)
  MenuBarFocusReason = Kee[int](6)
  OtherFocusReason = Kee[int](7)
  NoFocusReason = Kee[int](8)
