"""
ShortcutContext stands for the enum 'Qt::ShortcutContext' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ShortcutContext(CuteNum):
  """
  The enum 'Qt::ShortcutContext' of Qt, with the 4 names Qt gives in it.
  """

  WidgetShortcut = Kee[int](0)
  WindowShortcut = Kee[int](1)
  ApplicationShortcut = Kee[int](2)
  WidgetWithChildrenShortcut = Kee[int](3)
