"""
DockWidgetFeature stands for the flags enum 'QDockWidget::DockWidgetFeature'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qdockwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class DockWidgetFeature(CuteFlags):
  """
  The flags enum 'QDockWidget::DockWidgetFeature' of Qt, with the 7 names Qt
  gives in it. Qt names the type of its combinations
  'QDockWidget::DockWidgetFeatures'.
  """

  DockWidgetClosable = 0x1
  DockWidgetMovable = 0x2
  DockWidgetFloatable = 0x4
  DockWidgetVerticalTitleBar = 0x8
  DockWidgetFeatureMask = 0xf
  NoDockWidgetFeatures = 0x0
  Reserved = 0xff
