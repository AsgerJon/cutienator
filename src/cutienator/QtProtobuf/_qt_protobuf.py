"""
QtProtobuf stands for the namespace 'QtProtobuf' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QtProtobuf:
  """
  The namespace 'QtProtobuf' of Qt, which holds no objects. It holds the 1
  enums Qt writes in it, each under its name, and the 0 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class WireTypes(CuteNum, scoped=True):
    """
    The enum 'QtProtobuf::WireTypes' of Qt, with the 7 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Unknown = Kee[int](-1)
    Varint = Kee[int](0)
    Fixed64 = Kee[int](1)
    LengthDelimited = Kee[int](2)
    StartGroup = Kee[int](3)
    EndGroup = Kee[int](4)
    Fixed32 = Kee[int](5)
