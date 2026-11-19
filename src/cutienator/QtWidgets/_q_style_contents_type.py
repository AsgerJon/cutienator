"""
ContentsType stands for the enum 'QStyle::ContentsType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ContentsType(CuteNum):
  """
  The enum 'QStyle::ContentsType' of Qt, with the 24 names Qt gives in it.
  """

  CT_PushButton = Kee[int](0)
  CT_CheckBox = Kee[int](1)
  CT_RadioButton = Kee[int](2)
  CT_ToolButton = Kee[int](3)
  CT_ComboBox = Kee[int](4)
  CT_Splitter = Kee[int](5)
  CT_ProgressBar = Kee[int](6)
  CT_MenuItem = Kee[int](7)
  CT_MenuBarItem = Kee[int](8)
  CT_MenuBar = Kee[int](9)
  CT_Menu = Kee[int](10)
  CT_TabBarTab = Kee[int](11)
  CT_Slider = Kee[int](12)
  CT_ScrollBar = Kee[int](13)
  CT_LineEdit = Kee[int](14)
  CT_SpinBox = Kee[int](15)
  CT_SizeGrip = Kee[int](16)
  CT_TabWidget = Kee[int](17)
  CT_DialogButtons = Kee[int](18)
  CT_HeaderSection = Kee[int](19)
  CT_GroupBox = Kee[int](20)
  CT_MdiControls = Kee[int](21)
  CT_ItemViewItem = Kee[int](22)
  CT_CustomBase = Kee[int](4026531840)
