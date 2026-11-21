"""
GestureCancelPolicy stands for the enum 'QGesture::GestureCancelPolicy' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class GestureCancelPolicy(CuteNum):
  """
  The enum 'QGesture::GestureCancelPolicy' of Qt, with the 2 names Qt gives
  in it.
  """

  CancelNone = Kee[int](0)
  CancelAllInContext = Kee[int](1)
