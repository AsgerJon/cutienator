"""
Scope stands for the enum 'QSettings::Scope' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qsettings.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Scope(CuteNum):
  """
  The enum 'QSettings::Scope' of Qt, with the 2 names Qt gives in it.
  """

  UserScope = Kee[int](0)
  SystemScope = Kee[int](1)
