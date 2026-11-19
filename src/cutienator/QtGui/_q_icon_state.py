"""
State stands for the enum 'QIcon::State' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qicon.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class State(CuteNum):
  """
  The enum 'QIcon::State' of Qt, with the 2 names Qt gives in it.
  """

  On = Kee[int](0)
  Off = Kee[int](1)
