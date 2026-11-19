"""
OptionType stands for the enum 'QStyleOption::OptionType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class OptionType(CuteNum):
  """
  The enum 'QStyleOption::OptionType' of Qt, with the 26 names Qt gives in
  it.
  """

  SO_Default = Kee[int](0)
  SO_FocusRect = Kee[int](1)
  SO_Button = Kee[int](2)
  SO_Tab = Kee[int](3)
  SO_MenuItem = Kee[int](4)
  SO_Frame = Kee[int](5)
  SO_ProgressBar = Kee[int](6)
  SO_ToolBox = Kee[int](7)
  SO_Header = Kee[int](8)
  SO_DockWidget = Kee[int](9)
  SO_ViewItem = Kee[int](10)
  SO_TabWidgetFrame = Kee[int](11)
  SO_TabBarBase = Kee[int](12)
  SO_RubberBand = Kee[int](13)
  SO_ToolBar = Kee[int](14)
  SO_GraphicsItem = Kee[int](15)
  SO_Complex = Kee[int](983040)
  SO_Slider = Kee[int](983041)
  SO_SpinBox = Kee[int](983042)
  SO_ToolButton = Kee[int](983043)
  SO_ComboBox = Kee[int](983044)
  SO_TitleBar = Kee[int](983045)
  SO_GroupBox = Kee[int](983046)
  SO_SizeGrip = Kee[int](983047)
  SO_CustomBase = Kee[int](3840)
  SO_ComplexCustomBase = Kee[int](251658240)
