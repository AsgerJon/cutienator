"""
QtProtobufPrivate stands for the namespace 'QtProtobufPrivate' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class QtProtobufPrivate:
  """
  The namespace 'QtProtobufPrivate' of Qt, which holds no objects. It holds
  the 1 enums Qt writes in it, each under its name, and the 1 names Qt has
  for the combinations of a flags enum, each holding the class of that enum.
  It is never made into an object.
  """

  class FieldFlag(CuteFlags, number='unsigned int', scoped=True):
    """
    The flags enum 'QtProtobufPrivate::FieldFlag' of Qt, with the 9 names Qt
    gives in it. Qt names the type of its combinations
    'QtProtobufPrivate::FieldFlags'. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    NoFlags = 0x0
    NonPacked = 0x1
    Oneof = 0x2
    Optional = 0x4
    ExplicitPresence = 0x8
    Message = 0x10
    Enum = 0x20
    Repeated = 0x40
    Map = 0x80

  FieldFlags = FieldFlag
