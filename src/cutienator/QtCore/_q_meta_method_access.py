"""
Access stands for the enum 'QMetaMethod::Access' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qmetaobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Access(CuteNum):
  """
  The enum 'QMetaMethod::Access' of Qt, with the 3 names Qt gives in it.
  """

  Private = Kee[int](0)
  Protected = Kee[int](1)
  Public = Kee[int](2)
