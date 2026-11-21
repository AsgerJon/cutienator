"""
Type stands for the enum 'QJsonValue::Type' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qjsonvalue.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Type(CuteNum):
  """
  The enum 'QJsonValue::Type' of Qt, with the 7 names Qt gives in it.
  """

  Null = Kee[int](0)
  Bool = Kee[int](1)
  Double = Kee[int](2)
  String = Kee[int](3)
  Array = Kee[int](4)
  Object = Kee[int](5)
  Undefined = Kee[int](128)
