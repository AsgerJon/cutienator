"""
ScrollMode stands for the enum 'QAbstractItemView::ScrollMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qabstractitemview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ScrollMode(CuteNum):
  """
  The enum 'QAbstractItemView::ScrollMode' of Qt, with the 2 names Qt gives
  in it.
  """

  ScrollPerItem = Kee[int](0)
  ScrollPerPixel = Kee[int](1)
