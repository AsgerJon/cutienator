"""
PrimitiveElement stands for the enum 'QStyle::PrimitiveElement' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class PrimitiveElement(CuteNum):
  """
  The enum 'QStyle::PrimitiveElement' of Qt, with the 52 names Qt gives in
  it.
  """

  PE_Frame = Kee[int](0)
  PE_FrameDefaultButton = Kee[int](1)
  PE_FrameDockWidget = Kee[int](2)
  PE_FrameFocusRect = Kee[int](3)
  PE_FrameGroupBox = Kee[int](4)
  PE_FrameLineEdit = Kee[int](5)
  PE_FrameMenu = Kee[int](6)
  PE_FrameStatusBarItem = Kee[int](7)
  PE_FrameTabWidget = Kee[int](8)
  PE_FrameWindow = Kee[int](9)
  PE_FrameButtonBevel = Kee[int](10)
  PE_FrameButtonTool = Kee[int](11)
  PE_FrameTabBarBase = Kee[int](12)
  PE_PanelButtonCommand = Kee[int](13)
  PE_PanelButtonBevel = Kee[int](14)
  PE_PanelButtonTool = Kee[int](15)
  PE_PanelMenuBar = Kee[int](16)
  PE_PanelToolBar = Kee[int](17)
  PE_PanelLineEdit = Kee[int](18)
  PE_IndicatorArrowDown = Kee[int](19)
  PE_IndicatorArrowLeft = Kee[int](20)
  PE_IndicatorArrowRight = Kee[int](21)
  PE_IndicatorArrowUp = Kee[int](22)
  PE_IndicatorBranch = Kee[int](23)
  PE_IndicatorButtonDropDown = Kee[int](24)
  PE_IndicatorItemViewItemCheck = Kee[int](25)
  PE_IndicatorCheckBox = Kee[int](26)
  PE_IndicatorDockWidgetResizeHandle = Kee[int](27)
  PE_IndicatorHeaderArrow = Kee[int](28)
  PE_IndicatorMenuCheckMark = Kee[int](29)
  PE_IndicatorProgressChunk = Kee[int](30)
  PE_IndicatorRadioButton = Kee[int](31)
  PE_IndicatorSpinDown = Kee[int](32)
  PE_IndicatorSpinMinus = Kee[int](33)
  PE_IndicatorSpinPlus = Kee[int](34)
  PE_IndicatorSpinUp = Kee[int](35)
  PE_IndicatorToolBarHandle = Kee[int](36)
  PE_IndicatorToolBarSeparator = Kee[int](37)
  PE_PanelTipLabel = Kee[int](38)
  PE_IndicatorTabTear = Kee[int](39)
  PE_IndicatorTabTearLeft = Kee[int](39)
  PE_PanelScrollAreaCorner = Kee[int](40)
  PE_Widget = Kee[int](41)
  PE_IndicatorColumnViewArrow = Kee[int](42)
  PE_IndicatorItemViewItemDrop = Kee[int](43)
  PE_PanelItemViewItem = Kee[int](44)
  PE_PanelItemViewRow = Kee[int](45)
  PE_PanelStatusBar = Kee[int](46)
  PE_IndicatorTabClose = Kee[int](47)
  PE_PanelMenu = Kee[int](48)
  PE_IndicatorTabTearRight = Kee[int](49)
  PE_CustomBase = Kee[int](251658240)
