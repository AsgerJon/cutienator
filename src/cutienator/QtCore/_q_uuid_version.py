"""
Version stands for the enum 'QUuid::Version' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of QtCore/quuid.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Version(CuteNum):
  """
  The enum 'QUuid::Version' of Qt, with the 8 names Qt gives in it.
  """

  VerUnknown = Kee[int](-1)
  Time = Kee[int](1)
  EmbeddedPOSIX = Kee[int](2)
  Md5 = Kee[int](3)
  Name = Kee[int](3)
  Random = Kee[int](4)
  Sha1 = Kee[int](5)
  UnixEpoch = Kee[int](7)
