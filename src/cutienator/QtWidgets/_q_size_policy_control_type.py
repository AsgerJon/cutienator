"""
ControlType stands for the flags enum 'QSizePolicy::ControlType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qsizepolicy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ControlType(CuteFlags):
  """
  The flags enum 'QSizePolicy::ControlType' of Qt, with the 15 names Qt gives
  in it. Qt names the type of its combinations 'QSizePolicy::ControlTypes'.
  """

  DefaultType = 0x1
  ButtonBox = 0x2
  CheckBox = 0x4
  ComboBox = 0x8
  Frame = 0x10
  GroupBox = 0x20
  Label = 0x40
  Line = 0x80
  LineEdit = 0x100
  PushButton = 0x200
  RadioButton = 0x400
  Slider = 0x800
  SpinBox = 0x1000
  TabWidget = 0x2000
  ToolButton = 0x4000
