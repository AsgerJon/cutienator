"""
RenderFlag stands for the flags enum 'QWidget::RenderFlag' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class RenderFlag(CuteFlags):
  """
  The flags enum 'QWidget::RenderFlag' of Qt, with the 3 names Qt gives in
  it. Qt names the type of its combinations 'QWidget::RenderFlags'.
  """

  DrawWindowBackground = 0x1
  DrawChildren = 0x2
  IgnoreMask = 0x4
