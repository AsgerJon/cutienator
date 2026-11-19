"""
MouseEventSource stands for the enum 'Qt::MouseEventSource' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MouseEventSource(CuteNum):
  """
  The enum 'Qt::MouseEventSource' of Qt, with the 4 names Qt gives in it.
  """

  MouseEventNotSynthesized = Kee[int](0)
  MouseEventSynthesizedBySystem = Kee[int](1)
  MouseEventSynthesizedByQt = Kee[int](2)
  MouseEventSynthesizedByApplication = Kee[int](3)
