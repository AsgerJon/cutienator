"""
ToolButtonFeature stands for the flags enum
'QStyleOptionToolButton::ToolButtonFeature' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ToolButtonFeature(CuteFlags):
  """
  The flags enum 'QStyleOptionToolButton::ToolButtonFeature' of Qt, with the
  6 names Qt gives in it. Qt names the type of its combinations
  'QStyleOptionToolButton::ToolButtonFeatures'.
  """

  NULL = 0x0
  Arrow = 0x1
  Menu = 0x4
  MenuButtonPopup = 0x4
  PopupDelay = 0x8
  HasMenu = 0x10
