"""
Format stands for the enum 'QSettings::Format' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qsettings.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Format(CuteNum):
  """
  The enum 'QSettings::Format' of Qt, with the 19 names Qt gives in it.
  """

  NativeFormat = Kee[int](0)
  IniFormat = Kee[int](1)
  InvalidFormat = Kee[int](16)
  CustomFormat1 = Kee[int](17)
  CustomFormat2 = Kee[int](18)
  CustomFormat3 = Kee[int](19)
  CustomFormat4 = Kee[int](20)
  CustomFormat5 = Kee[int](21)
  CustomFormat6 = Kee[int](22)
  CustomFormat7 = Kee[int](23)
  CustomFormat8 = Kee[int](24)
  CustomFormat9 = Kee[int](25)
  CustomFormat10 = Kee[int](26)
  CustomFormat11 = Kee[int](27)
  CustomFormat12 = Kee[int](28)
  CustomFormat13 = Kee[int](29)
  CustomFormat14 = Kee[int](30)
  CustomFormat15 = Kee[int](31)
  CustomFormat16 = Kee[int](32)
