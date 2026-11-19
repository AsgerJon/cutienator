"""
ColorScheme stands for the enum 'Qt::ColorScheme' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ColorScheme(CuteNum, scoped=True):
  """
  The enum 'Qt::ColorScheme' of Qt, with the 3 names Qt gives in it. C++
  keeps these names inside the enum, so the class that holds the enum does
  not have them.
  """

  Unknown = Kee[int](0)
  Light = Kee[int](1)
  Dark = Kee[int](2)
