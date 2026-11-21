"""
Endian stands for the enum 'QSysInfo::Endian' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qsysinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Endian(CuteNum):
  """
  The enum 'QSysInfo::Endian' of Qt, with the 3 names Qt gives in it.
  """

  BigEndian = Kee[int](0)
  LittleEndian = Kee[int](1)
  ByteOrder = Kee[int](1)
