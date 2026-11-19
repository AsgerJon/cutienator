"""
ControlElement stands for the enum 'QStyle::ControlElement' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ControlElement(CuteNum):
  """
  The enum 'QStyle::ControlElement' of Qt, with the 48 names Qt gives in it.
  """

  CE_PushButton = Kee[int](0)
  CE_PushButtonBevel = Kee[int](1)
  CE_PushButtonLabel = Kee[int](2)
  CE_CheckBox = Kee[int](3)
  CE_CheckBoxLabel = Kee[int](4)
  CE_RadioButton = Kee[int](5)
  CE_RadioButtonLabel = Kee[int](6)
  CE_TabBarTab = Kee[int](7)
  CE_TabBarTabShape = Kee[int](8)
  CE_TabBarTabLabel = Kee[int](9)
  CE_ProgressBar = Kee[int](10)
  CE_ProgressBarGroove = Kee[int](11)
  CE_ProgressBarContents = Kee[int](12)
  CE_ProgressBarLabel = Kee[int](13)
  CE_MenuItem = Kee[int](14)
  CE_MenuScroller = Kee[int](15)
  CE_MenuVMargin = Kee[int](16)
  CE_MenuHMargin = Kee[int](17)
  CE_MenuTearoff = Kee[int](18)
  CE_MenuEmptyArea = Kee[int](19)
  CE_MenuBarItem = Kee[int](20)
  CE_MenuBarEmptyArea = Kee[int](21)
  CE_ToolButtonLabel = Kee[int](22)
  CE_Header = Kee[int](23)
  CE_HeaderSection = Kee[int](24)
  CE_HeaderLabel = Kee[int](25)
  CE_ToolBoxTab = Kee[int](26)
  CE_SizeGrip = Kee[int](27)
  CE_Splitter = Kee[int](28)
  CE_RubberBand = Kee[int](29)
  CE_DockWidgetTitle = Kee[int](30)
  CE_ScrollBarAddLine = Kee[int](31)
  CE_ScrollBarSubLine = Kee[int](32)
  CE_ScrollBarAddPage = Kee[int](33)
  CE_ScrollBarSubPage = Kee[int](34)
  CE_ScrollBarSlider = Kee[int](35)
  CE_ScrollBarFirst = Kee[int](36)
  CE_ScrollBarLast = Kee[int](37)
  CE_FocusFrame = Kee[int](38)
  CE_ComboBoxLabel = Kee[int](39)
  CE_ToolBar = Kee[int](40)
  CE_ToolBoxTabShape = Kee[int](41)
  CE_ToolBoxTabLabel = Kee[int](42)
  CE_HeaderEmptyArea = Kee[int](43)
  CE_ColumnViewGrip = Kee[int](44)
  CE_ItemViewItem = Kee[int](45)
  CE_ShapedFrame = Kee[int](46)
  CE_CustomBase = Kee[int](4026531840)
