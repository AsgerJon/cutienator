"""
Base64DecodingStatus stands for the enum 'QByteArray::Base64DecodingStatus'
of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qbytearray.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class Base64DecodingStatus(CuteNum, scoped=True):
  """
  The enum 'QByteArray::Base64DecodingStatus' of Qt, with the 4 names Qt
  gives in it. C++ keeps these names inside the enum, so the class that holds
  the enum does not have them.
  """

  Ok = Kee[int](0)
  IllegalInputLength = Kee[int](1)
  IllegalCharacter = Kee[int](2)
  IllegalPadding = Kee[int](3)
