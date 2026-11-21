"""
TabFeature stands for the flags enum 'QStyleOptionTab::TabFeature' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class TabFeature(CuteFlags):
  """
  The flags enum 'QStyleOptionTab::TabFeature' of Qt, with the 3 names Qt
  gives in it. Qt names the type of its combinations
  'QStyleOptionTab::TabFeatures'.
  """

  NULL = 0x0
  HasFrame = 0x1
  MinimumSizeHint = 0x2
