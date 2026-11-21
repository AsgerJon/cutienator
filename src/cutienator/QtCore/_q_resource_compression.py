"""
Compression stands for the enum 'QResource::Compression' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qresource.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Compression(CuteNum):
  """
  The enum 'QResource::Compression' of Qt, with the 3 names Qt gives in it.
  """

  NoCompression = Kee[int](0)
  ZlibCompression = Kee[int](1)
  ZstdCompression = Kee[int](2)
