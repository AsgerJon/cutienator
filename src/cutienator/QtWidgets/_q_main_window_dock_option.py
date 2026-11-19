"""
DockOption stands for the flags enum 'QMainWindow::DockOption' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qmainwindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class DockOption(CuteFlags):
  """
  The flags enum 'QMainWindow::DockOption' of Qt, with the 6 names Qt gives
  in it. Qt names the type of its combinations 'QMainWindow::DockOptions'.
  """

  AnimatedDocks = 0x1
  AllowNestedDocks = 0x2
  AllowTabbedDocks = 0x4
  ForceTabbedDocks = 0x8
  VerticalTabs = 0x10
  GroupedDragging = 0x20
