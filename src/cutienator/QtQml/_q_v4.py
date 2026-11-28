"""
QV4 stands for the namespace 'QV4' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum


class QV4:
  """
  The namespace 'QV4' of Qt, which holds no objects. It holds the 8 enums Qt
  writes in it, each under its name, and the 1 names Qt has for the
  combinations of a flags enum, each holding the class of that enum. It is
  never made into an object.
  """

  class AtomicModifyOps(CuteNum):
    """
    The enum 'QV4::AtomicModifyOps' of Qt, with the 7 names Qt gives in it.
    """

    AtomicAdd = Kee[int](0)
    AtomicAnd = Kee[int](1)
    AtomicExchange = Kee[int](2)
    AtomicOr = Kee[int](3)
    AtomicSub = Kee[int](4)
    AtomicXor = Kee[int](5)
    NAtomicModifyOps = Kee[int](6)

  class CoercionProblem(CuteNum):
    """
    The enum 'QV4::CoercionProblem' of Qt, with the 2 names Qt gives in it.
    """

    InsufficientAnnotation = Kee[int](0)
    InvalidListType = Kee[int](1)

  class GeneratorState(CuteNum, scoped=True):
    """
    The enum 'QV4::GeneratorState' of Qt, with the 5 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Undefined = Kee[int](0)
    SuspendedStart = Kee[int](1)
    SuspendedYield = Kee[int](2)
    Executing = Kee[int](3)
    Completed = Kee[int](4)

  class IteratorKind(CuteNum):
    """
    The enum 'QV4::IteratorKind' of Qt, with the 3 names Qt gives in it.
    """

    KeyIteratorKind = Kee[int](0)
    ValueIteratorKind = Kee[int](1)
    KeyValueIteratorKind = Kee[int](2)

  class ObjectLiteralArgument(CuteNum, scoped=True):
    """
    The enum 'QV4::ObjectLiteralArgument' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Value = Kee[int](0)
    Method = Kee[int](1)
    Getter = Kee[int](2)
    Setter = Kee[int](3)

  class PropertyFlag(CuteFlags):
    """
    The flags enum 'QV4::PropertyFlag' of Qt, with the 8 names Qt gives in
    it. Qt names the type of its combinations 'QV4::PropertyFlags'.
    """

    Attr_Data = 0x0
    Attr_Accessor = 0x1
    Attr_NotWritable = 0x2
    Attr_NotEnumerable = 0x4
    Attr_NotConfigurable = 0x8
    Attr_ReadOnly = 0xe
    Attr_ReadOnly_ButConfigurable = 0x6
    Attr_Invalid = 0xff

  PropertyFlags = PropertyFlag

  class TypeHint(CuteNum):
    """The enum 'QV4::TypeHint' of Qt, with the 3 names Qt gives in it."""

    PREFERREDTYPE_HINT = Kee[int](0)
    NUMBER_HINT = Kee[int](1)
    STRING_HINT = Kee[int](2)

  class TypedArrayType(CuteNum):
    """
    The enum 'QV4::TypedArrayType' of Qt, with the 10 names Qt gives in it.
    """

    Int8Array = Kee[int](0)
    UInt8Array = Kee[int](1)
    Int16Array = Kee[int](2)
    UInt16Array = Kee[int](3)
    Int32Array = Kee[int](4)
    UInt32Array = Kee[int](5)
    UInt8ClampedArray = Kee[int](6)
    Float32Array = Kee[int](7)
    Float64Array = Kee[int](8)
    NTypedArrayTypes = Kee[int](9)
