"""
LayoutMode stands for the enum 'QListView::LayoutMode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qlistview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class LayoutMode(CuteNum):
  """
  The enum 'QListView::LayoutMode' of Qt, with the 2 names Qt gives in it.
  """

  SinglePass = Kee[int](0)
  Batched = Kee[int](1)
