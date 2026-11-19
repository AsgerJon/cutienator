"""
ResizeMode stands for the enum 'QHeaderView::ResizeMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qheaderview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ResizeMode(CuteNum):
  """
  The enum 'QHeaderView::ResizeMode' of Qt, with the 5 names Qt gives in it.
  """

  Interactive = Kee[int](0)
  Stretch = Kee[int](1)
  Fixed = Kee[int](2)
  ResizeToContents = Kee[int](3)
  Custom = Kee[int](2)
