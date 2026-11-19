"""
Call stands for the enum 'QMetaObject::Call' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qobjectdefs.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Call(CuteNum):
  """
  The enum 'QMetaObject::Call' of Qt, with the 11 names Qt gives in it.
  """

  InvokeMetaMethod = Kee[int](0)
  ReadProperty = Kee[int](1)
  WriteProperty = Kee[int](2)
  ResetProperty = Kee[int](3)
  CreateInstance = Kee[int](4)
  IndexOfMethod = Kee[int](5)
  RegisterPropertyMetaType = Kee[int](6)
  RegisterMethodArgumentMetaType = Kee[int](7)
  BindableProperty = Kee[int](8)
  CustomCall = Kee[int](9)
  ConstructInPlace = Kee[int](10)
