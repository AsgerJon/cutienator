"""
TagSeparator stands for the enum 'QLocale::TagSeparator' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qlocale.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class TagSeparator(CuteNum, scoped=True):
  """
  The enum 'QLocale::TagSeparator' of Qt, with the 2 names Qt gives in it.
  C++ keeps these names inside the enum, so the class that holds the enum
  does not have them.
  """

  Dash = Kee[int](45)
  Underscore = Kee[int](95)
