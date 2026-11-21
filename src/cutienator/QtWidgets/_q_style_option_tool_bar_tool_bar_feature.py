"""
ToolBarFeature stands for the flags enum
'QStyleOptionToolBar::ToolBarFeature' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ToolBarFeature(CuteFlags):
  """
  The flags enum 'QStyleOptionToolBar::ToolBarFeature' of Qt, with the 2
  names Qt gives in it. Qt names the type of its combinations
  'QStyleOptionToolBar::ToolBarFeatures'.
  """

  NULL = 0x0
  Movable = 0x1
