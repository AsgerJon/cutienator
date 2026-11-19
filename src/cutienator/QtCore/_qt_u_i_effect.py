"""
UIEffect stands for the enum 'Qt::UIEffect' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class UIEffect(CuteNum):
  """
  The enum 'Qt::UIEffect' of Qt, with the 7 names Qt gives in it.
  """

  UI_General = Kee[int](0)
  UI_AnimateMenu = Kee[int](1)
  UI_FadeMenu = Kee[int](2)
  UI_AnimateCombo = Kee[int](3)
  UI_AnimateTooltip = Kee[int](4)
  UI_FadeTooltip = Kee[int](5)
  UI_AnimateToolBox = Kee[int](6)
