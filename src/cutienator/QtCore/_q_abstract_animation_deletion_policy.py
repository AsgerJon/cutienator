"""
DeletionPolicy stands for the enum 'QAbstractAnimation::DeletionPolicy' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qabstractanimation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class DeletionPolicy(CuteNum):
  """
  The enum 'QAbstractAnimation::DeletionPolicy' of Qt, with the 2 names Qt
  gives in it.
  """

  KeepWhenStopped = Kee[int](0)
  DeleteWhenStopped = Kee[int](1)
