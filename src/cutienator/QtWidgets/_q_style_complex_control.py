"""
ComplexControl stands for the enum 'QStyle::ComplexControl' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ComplexControl(CuteNum):
  """
  The enum 'QStyle::ComplexControl' of Qt, with the 10 names Qt gives in it.
  """

  CC_SpinBox = Kee[int](0)
  CC_ComboBox = Kee[int](1)
  CC_ScrollBar = Kee[int](2)
  CC_Slider = Kee[int](3)
  CC_ToolButton = Kee[int](4)
  CC_TitleBar = Kee[int](5)
  CC_Dial = Kee[int](6)
  CC_GroupBox = Kee[int](7)
  CC_MdiControls = Kee[int](8)
  CC_CustomBase = Kee[int](4026531840)
