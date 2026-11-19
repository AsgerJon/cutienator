"""
Attributes stands for the enum 'QMetaMethod::Attributes' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qmetaobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Attributes(CuteNum):
  """
  The enum 'QMetaMethod::Attributes' of Qt, with the 3 names Qt gives in it.
  """

  Compatibility = Kee[int](1)
  Cloned = Kee[int](2)
  Scriptable = Kee[int](4)
