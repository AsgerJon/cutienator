"""
SubControl stands for the flags enum 'QStyle::SubControl' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class SubControl(CuteFlags, number='unsigned int'):
  """
  The flags enum 'QStyle::SubControl' of Qt, with the 43 names Qt gives in
  it. Qt names the type of its combinations 'QStyle::SubControls'.
  """

  SC_None = 0x0
  SC_ScrollBarAddLine = 0x1
  SC_ScrollBarSubLine = 0x2
  SC_ScrollBarAddPage = 0x4
  SC_ScrollBarSubPage = 0x8
  SC_ScrollBarFirst = 0x10
  SC_ScrollBarLast = 0x20
  SC_ScrollBarSlider = 0x40
  SC_ScrollBarGroove = 0x80
  SC_SpinBoxUp = 0x1
  SC_SpinBoxDown = 0x2
  SC_SpinBoxFrame = 0x4
  SC_SpinBoxEditField = 0x8
  SC_ComboBoxFrame = 0x1
  SC_ComboBoxEditField = 0x2
  SC_ComboBoxArrow = 0x4
  SC_ComboBoxListBoxPopup = 0x8
  SC_SliderGroove = 0x1
  SC_SliderHandle = 0x2
  SC_SliderTickmarks = 0x4
  SC_ToolButton = 0x1
  SC_ToolButtonMenu = 0x2
  SC_TitleBarSysMenu = 0x1
  SC_TitleBarMinButton = 0x2
  SC_TitleBarMaxButton = 0x4
  SC_TitleBarCloseButton = 0x8
  SC_TitleBarNormalButton = 0x10
  SC_TitleBarShadeButton = 0x20
  SC_TitleBarUnshadeButton = 0x40
  SC_TitleBarContextHelpButton = 0x80
  SC_TitleBarLabel = 0x100
  SC_DialGroove = 0x1
  SC_DialHandle = 0x2
  SC_DialTickmarks = 0x4
  SC_GroupBoxCheckBox = 0x1
  SC_GroupBoxLabel = 0x2
  SC_GroupBoxContents = 0x4
  SC_GroupBoxFrame = 0x8
  SC_MdiMinButton = 0x1
  SC_MdiNormalButton = 0x2
  SC_MdiCloseButton = 0x4
  SC_CustomBase = 0xf0000000
  SC_All = 0xffffffff
