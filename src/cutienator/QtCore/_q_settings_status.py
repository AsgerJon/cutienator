"""
Status stands for the enum 'QSettings::Status' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qsettings.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Status(CuteNum):
  """
  The enum 'QSettings::Status' of Qt, with the 3 names Qt gives in it.
  """

  NoError = Kee[int](0)
  AccessError = Kee[int](1)
  FormatError = Kee[int](2)
