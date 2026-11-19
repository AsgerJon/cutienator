"""
Visibility stands for the enum 'QWindow::Visibility' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qwindow.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Visibility(CuteNum):
  """
  The enum 'QWindow::Visibility' of Qt, with the 6 names Qt gives in it.
  """

  Hidden = Kee[int](0)
  AutomaticVisibility = Kee[int](1)
  Windowed = Kee[int](2)
  Minimized = Kee[int](3)
  Maximized = Kee[int](4)
  FullScreen = Kee[int](5)
