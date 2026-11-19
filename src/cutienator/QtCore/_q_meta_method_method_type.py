"""
MethodType stands for the enum 'QMetaMethod::MethodType' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qmetaobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class MethodType(CuteNum):
  """
  The enum 'QMetaMethod::MethodType' of Qt, with the 4 names Qt gives in it.
  """

  Method = Kee[int](0)
  Signal = Kee[int](1)
  Slot = Kee[int](2)
  Constructor = Kee[int](3)
