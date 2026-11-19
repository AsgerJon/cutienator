"""
NavigationMode stands for the enum 'Qt::NavigationMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class NavigationMode(CuteNum):
  """
  The enum 'Qt::NavigationMode' of Qt, with the 5 names Qt gives in it.
  """

  NavigationModeNone = Kee[int](0)
  NavigationModeKeypadTabOrder = Kee[int](1)
  NavigationModeKeypadDirectional = Kee[int](2)
  NavigationModeCursorAuto = Kee[int](3)
  NavigationModeCursorForceVisible = Kee[int](4)
