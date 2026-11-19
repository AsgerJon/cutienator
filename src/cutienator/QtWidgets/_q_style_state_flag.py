"""
StateFlag stands for the flags enum 'QStyle::StateFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyle.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class StateFlag(CuteFlags):
  """
  The flags enum 'QStyle::StateFlag' of Qt, with the 28 names Qt gives in it.
  Qt names the type of its combinations 'QStyle::State'.
  """

  State_None = 0x0
  State_Enabled = 0x1
  State_Raised = 0x2
  State_Sunken = 0x4
  State_Off = 0x8
  State_NoChange = 0x10
  State_On = 0x20
  State_DownArrow = 0x40
  State_Horizontal = 0x80
  State_HasFocus = 0x100
  State_Top = 0x200
  State_Bottom = 0x400
  State_FocusAtBorder = 0x800
  State_AutoRaise = 0x1000
  State_MouseOver = 0x2000
  State_UpArrow = 0x4000
  State_Selected = 0x8000
  State_Active = 0x10000
  State_Window = 0x20000
  State_Open = 0x40000
  State_Children = 0x80000
  State_Item = 0x100000
  State_Sibling = 0x200000
  State_Editing = 0x400000
  State_KeyboardFocusChange = 0x800000
  State_ReadOnly = 0x2000000
  State_Small = 0x4000000
  State_Mini = 0x8000000
