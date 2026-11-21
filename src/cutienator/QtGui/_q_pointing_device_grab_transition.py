"""
GrabTransition stands for the enum 'QPointingDevice::GrabTransition' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qpointingdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class GrabTransition(CuteNum):
  """
  The enum 'QPointingDevice::GrabTransition' of Qt, with the 7 names Qt gives
  in it.
  """

  GrabPassive = Kee[int](1)
  UngrabPassive = Kee[int](2)
  CancelGrabPassive = Kee[int](3)
  OverrideGrabPassive = Kee[int](4)
  GrabExclusive = Kee[int](16)
  UngrabExclusive = Kee[int](32)
  CancelGrabExclusive = Kee[int](48)
