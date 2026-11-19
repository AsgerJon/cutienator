"""
Mode stands for the enum 'QIcon::Mode' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtGui/qicon.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Mode(CuteNum):
  """
  The enum 'QIcon::Mode' of Qt, with the 4 names Qt gives in it.
  """

  Normal = Kee[int](0)
  Disabled = Kee[int](1)
  Active = Kee[int](2)
  Selected = Kee[int](3)
