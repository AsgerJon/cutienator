"""
SubWindowOption stands for the flags enum 'QMdiSubWindow::SubWindowOption' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qmdisubwindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class SubWindowOption(CuteFlags):
  """
  The flags enum 'QMdiSubWindow::SubWindowOption' of Qt, with the 4 names Qt
  gives in it. Qt names the type of its combinations
  'QMdiSubWindow::SubWindowOptions'.
  """

  AllowOutsideAreaHorizontally = 0x1
  AllowOutsideAreaVertically = 0x2
  RubberBandResize = 0x4
  RubberBandMove = 0x8
