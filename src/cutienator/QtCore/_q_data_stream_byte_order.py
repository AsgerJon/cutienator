"""
ByteOrder stands for the enum 'QDataStream::ByteOrder' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qdatastream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ByteOrder(CuteNum):
  """
  The enum 'QDataStream::ByteOrder' of Qt, with the 2 names Qt gives in it.
  """

  BigEndian = Kee[int](0)
  LittleEndian = Kee[int](1)
