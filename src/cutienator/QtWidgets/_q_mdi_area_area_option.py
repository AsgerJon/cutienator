"""
AreaOption stands for the flags enum 'QMdiArea::AreaOption' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qmdiarea.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class AreaOption(CuteFlags):
  """
  The flags enum 'QMdiArea::AreaOption' of Qt, with the 1 names Qt gives in
  it. Qt names the type of its combinations 'QMdiArea::AreaOptions'.
  """

  DontMaximizeSubWindowOnActivation = 0x1
