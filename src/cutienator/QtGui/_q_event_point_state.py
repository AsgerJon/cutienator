"""
State stands for the flags enum 'QEventPoint::State' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtGui/qeventpoint.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class State(CuteFlags, number='unsigned char'):
  """
  The flags enum 'QEventPoint::State' of Qt, with the 5 names Qt gives in it.
  Qt names the type of its combinations 'QEventPoint::States'.
  """

  Unknown = 0x0
  Stationary = 0x4
  Pressed = 0x1
  Updated = 0x2
  Released = 0x8
