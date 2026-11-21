"""
WindowOrder stands for the enum 'QMdiArea::WindowOrder' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qmdiarea.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class WindowOrder(CuteNum):
  """
  The enum 'QMdiArea::WindowOrder' of Qt, with the 3 names Qt gives in it.
  """

  CreationOrder = Kee[int](0)
  StackingOrder = Kee[int](1)
  ActivationHistoryOrder = Kee[int](2)
