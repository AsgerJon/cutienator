"""
QtMocConstants stands for the namespace 'QtMocConstants' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class QtMocConstants:
  """
  The namespace 'QtMocConstants' of Qt, which holds no objects. It holds the
  5 enums Qt writes in it, each under its name, and the 0 names Qt has for
  the combinations of a flags enum, each holding the class of that enum. It
  is never made into an object.
  """

  class EnumFlags(CuteNum):
    """
    The enum 'QtMocConstants::EnumFlags' of Qt, with the 3 names Qt gives in
    it.
    """

    EnumIsFlag = Kee[int](1)
    EnumIsScoped = Kee[int](2)
    EnumIs64Bit = Kee[int](64)

  class MetaDataFlags(CuteNum):
    """
    The enum 'QtMocConstants::MetaDataFlags' of Qt, with the 3 names Qt gives
    in it.
    """

    IsUnresolvedType = Kee[int](2147483648)
    TypeNameIndexMask = Kee[int](2147483647)
    IsUnresolvedSignal = Kee[int](1879048192)

  class MetaObjectFlag(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QtMocConstants::MetaObjectFlag' of Qt, with the 4 names
    Qt gives in it. Qt names the type of its combinations 'MetaObjectFlags'.
    """

    DynamicMetaObject = 0x1
    RequiresVariantMetaObject = 0x2
    PropertyAccessInStaticMetaCall = 0x4
    AllocatedMetaObject = 0x8

  class MethodFlags(CuteNum):
    """
    The enum 'QtMocConstants::MethodFlags' of Qt, with the 14 names Qt gives
    in it.
    """

    AccessPrivate = Kee[int](0)
    AccessProtected = Kee[int](1)
    AccessPublic = Kee[int](2)
    AccessMask = Kee[int](3)
    MethodMethod = Kee[int](0)
    MethodSignal = Kee[int](4)
    MethodSlot = Kee[int](8)
    MethodConstructor = Kee[int](12)
    MethodTypeMask = Kee[int](12)
    MethodCompatibility = Kee[int](16)
    MethodCloned = Kee[int](32)
    MethodScriptable = Kee[int](64)
    MethodRevisioned = Kee[int](128)
    MethodIsConst = Kee[int](256)

  class PropertyFlags(CuteNum):
    """
    The enum 'QtMocConstants::PropertyFlags' of Qt, with the 17 names Qt
    gives in it.
    """

    Invalid = Kee[int](0)
    Readable = Kee[int](1)
    Writable = Kee[int](2)
    Resettable = Kee[int](4)
    EnumOrFlag = Kee[int](8)
    Alias = Kee[int](16)
    Virtual = Kee[int](32)
    Override = Kee[int](64)
    StdCppSet = Kee[int](256)
    Constant = Kee[int](1024)
    Final = Kee[int](2048)
    Designable = Kee[int](4096)
    Scriptable = Kee[int](16384)
    Stored = Kee[int](65536)
    User = Kee[int](1048576)
    Required = Kee[int](16777216)
    Bindable = Kee[int](33554432)
