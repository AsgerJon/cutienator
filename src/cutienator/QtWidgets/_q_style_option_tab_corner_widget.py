"""
CornerWidget stands for the flags enum 'QStyleOptionTab::CornerWidget' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class CornerWidget(CuteFlags):
  """
  The flags enum 'QStyleOptionTab::CornerWidget' of Qt, with the 3 names Qt
  gives in it. Qt names the type of its combinations
  'QStyleOptionTab::CornerWidgets'.
  """

  NoCornerWidgets = 0x0
  LeftCornerWidget = 0x1
  RightCornerWidget = 0x2
