"""
HitTestAccuracy stands for the enum 'Qt::HitTestAccuracy' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class HitTestAccuracy(CuteNum):
  """
  The enum 'Qt::HitTestAccuracy' of Qt, with the 2 names Qt gives in it.
  """

  ExactHit = Kee[int](0)
  FuzzyHit = Kee[int](1)
