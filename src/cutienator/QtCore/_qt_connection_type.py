"""
ConnectionType stands for the enum 'Qt::ConnectionType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class ConnectionType(CuteNum):
  """
  The enum 'Qt::ConnectionType' of Qt, with the 6 names Qt gives in it.
  """

  AutoConnection = Kee[int](0)
  DirectConnection = Kee[int](1)
  QueuedConnection = Kee[int](2)
  BlockingQueuedConnection = Kee[int](3)
  UniqueConnection = Kee[int](128)
  SingleShotConnection = Kee[int](256)
