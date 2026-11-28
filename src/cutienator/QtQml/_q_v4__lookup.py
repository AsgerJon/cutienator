"""
QV4::Lookup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4lookup_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::Lookup to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Lookup(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Lookup: a plain Python object standing in front
  of one C++ QV4::Lookup.

  C++ hands a QV4::Lookup around as a copy, so every C++ QV4::Lookup behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::Lookup that has a ritual and that Python can
  call so far, 35 names in all: 'resolveGetter', 'resolvePrimitiveGetter',
  'resolveGlobalGetter', 'resolveProtoGetter', 'getterGeneric',
  'getterTwoClasses', 'getterFallback', 'getter0MemberData', 'getter0Inline',
  'getterProto', 'getter0Inlinegetter0Inline',
  'getter0Inlinegetter0MemberData', 'getter0MemberDatagetter0MemberData',
  'getterProtoTwoClasses', 'getterAccessor', 'getterProtoAccessor',
  'getterProtoAccessorTwoClasses', 'getterIndexed', 'getterQObject',
  'getterQObjectMethod', 'getterFallbackMethod', 'getterValueType',
  'primitiveGetterProto', 'primitiveGetterAccessor', 'stringLengthGetter',
  'globalGetterGeneric', 'globalGetterProto', 'globalGetterProtoAccessor',
  'resolveSetter', 'markObjects', 'contextGetter', 'doCallGlobal',
  'globalGetter', 'getter', 'releasePropertyCache'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QV4::Lookup::setterGeneric(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QV4::Lookup::setterTwoClasses(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QV4::Lookup::setterFallback(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QV4::Lookup::setter0MemberData(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QV4::Lookup::setter0Inline(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QV4::Lookup::setter0setter0(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QV4::Lookup::setterInsert(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QV4::Lookup::setterQObject(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QV4::Lookup::arrayLengthSetter(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QV4::Lookup::setter(ExecutionEngine *engine, Value &object,
    const Value &value)': takes a type Python has no way to hand over yet.
  - Qt's 'QV4::Lookup::~Lookup()': the destructor: Python removes its C++
    QV4::Lookup by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::Lookup is created at the first use, not by
    'QV4::Lookup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Lookup back gives a copy the ritual made for
    Python, in a new cute QV4::Lookup.
  - Each name of Qt's QV4::Lookup that has no cute function yet,
    'arrayLengthSetter', 'setter', 'setter0Inline', 'setter0MemberData',
    'setter0setter0', 'setterFallback', 'setterGeneric', 'setterInsert',
    'setterQObject', 'setterTwoClasses', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::Lookup, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Call(CuteNum, scoped=True):
    """
    The enum 'QV4::Lookup::Call' of Qt, with the 51 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    ContextGetterContextObjectMethod = Kee[int](0)
    ContextGetterContextObjectProperty = Kee[int](1)
    ContextGetterGeneric = Kee[int](2)
    ContextGetterIdObject = Kee[int](3)
    ContextGetterIdObjectInParentContext = Kee[int](4)
    ContextGetterInGlobalObject = Kee[int](5)
    ContextGetterInParentContextHierarchy = Kee[int](6)
    ContextGetterScopeObjectMethod = Kee[int](7)
    ContextGetterScopeObjectProperty = Kee[int](8)
    ContextGetterScopeObjectPropertyFallback = Kee[int](9)
    ContextGetterScript = Kee[int](10)
    ContextGetterSingleton = Kee[int](11)
    ContextGetterType = Kee[int](12)
    ContextGetterValueSingleton = Kee[int](13)
    GlobalGetterGeneric = Kee[int](14)
    GlobalGetterProto = Kee[int](15)
    GlobalGetterProtoAccessor = Kee[int](16)
    Getter0Inline = Kee[int](17)
    Getter0InlineGetter0Inline = Kee[int](18)
    Getter0InlineGetter0MemberData = Kee[int](19)
    Getter0MemberData = Kee[int](20)
    Getter0MemberDataGetter0MemberData = Kee[int](21)
    GetterAccessor = Kee[int](22)
    GetterAccessorPrimitive = Kee[int](23)
    GetterEnum = Kee[int](24)
    GetterEnumValue = Kee[int](25)
    GetterGeneric = Kee[int](26)
    GetterIndexed = Kee[int](27)
    GetterProto = Kee[int](28)
    GetterProtoAccessor = Kee[int](29)
    GetterProtoAccessorTwoClasses = Kee[int](30)
    GetterProtoPrimitive = Kee[int](31)
    GetterProtoTwoClasses = Kee[int](32)
    GetterQObjectAttached = Kee[int](33)
    GetterQObjectMethod = Kee[int](34)
    GetterQObjectMethodFallback = Kee[int](35)
    GetterQObjectProperty = Kee[int](36)
    GetterQObjectPropertyFallback = Kee[int](37)
    GetterSingletonMethod = Kee[int](38)
    GetterSingletonProperty = Kee[int](39)
    GetterStringLength = Kee[int](40)
    GetterValueTypeProperty = Kee[int](41)
    Setter0Inline = Kee[int](42)
    Setter0MemberData = Kee[int](43)
    Setter0Setter0 = Kee[int](44)
    SetterArrayLength = Kee[int](45)
    SetterGeneric = Kee[int](46)
    SetterInsert = Kee[int](47)
    SetterQObjectProperty = Kee[int](48)
    SetterQObjectPropertyFallback = Kee[int](49)
    SetterValueTypeProperty = Kee[int](50)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getterGeneric(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getterGeneric(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#getterGeneric

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getterGeneric(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup13getterGenericEPS0_PNS_15ExecutionEngineERKNS'
        '_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getterTwoClasses(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getterTwoClasses(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#getterTwoClasses

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getterTwoClasses(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup16getterTwoClassesEPS0_PNS_15ExecutionEngineER'
        'KNS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getterFallback(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getterFallback(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#getterFallback

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getterFallback(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup14getterFallbackEPS0_PNS_15ExecutionEngineERKN'
        'S_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getter0MemberData(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getter0MemberData(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#getter0MemberData

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getter0MemberData(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup17getter0MemberDataEPS0_PNS_15ExecutionEngineE'
        'RKNS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getter0Inline(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getter0Inline(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#getter0Inline

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getter0Inline(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup13getter0InlineEPS0_PNS_15ExecutionEngineERKNS'
        '_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getterProto(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getterProto(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#getterProto

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getterProto(Lookup *lookup, ExecutionEngine
    #      *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup11getterProtoEPS0_PNS_15ExecutionEngineERKNS_5'
        'ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getter0Inlinegetter0Inline(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getter0Inlinegetter0Inline(Lookup
    *lookup, ExecutionEngine *engine, const Value &object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#getter0Inlinegetter0Inline

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getter0Inlinegetter0Inline(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup26getter0Inlinegetter0InlineEPS0_PNS_15Executi'
        'onEngineERKNS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getter0Inlinegetter0MemberData(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::Lookup::getter0Inlinegetter0MemberData(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#getter0Inlinegetter0MemberData

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getter0Inlinegetter0MemberData(Lookup
    #      *lookup, ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup30getter0Inlinegetter0MemberDataEPS0_PNS_15Exe'
        'cutionEngineERKNS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getter0MemberDatagetter0MemberData(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::Lookup::getter0MemberDatagetter0MemberData(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#getter0MemberDatagetter0MemberData

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getter0MemberDatagetter0MemberData(Lookup
    #      *lookup, ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup34getter0MemberDatagetter0MemberDataEPS0_PNS_1'
        '5ExecutionEngineERKNS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getterProtoTwoClasses(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getterProtoTwoClasses(Lookup
    *lookup, ExecutionEngine *engine, const Value &object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#getterProtoTwoClasses

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getterProtoTwoClasses(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup21getterProtoTwoClassesEPS0_PNS_15ExecutionEng'
        'ineERKNS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getterAccessor(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getterAccessor(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#getterAccessor

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getterAccessor(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup14getterAccessorEPS0_PNS_15ExecutionEngineERKN'
        'S_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getterProtoAccessor(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getterProtoAccessor(Lookup
    *lookup, ExecutionEngine *engine, const Value &object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#getterProtoAccessor

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getterProtoAccessor(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup19getterProtoAccessorEPS0_PNS_15ExecutionEngin'
        'eERKNS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getterProtoAccessorTwoClasses(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::Lookup::getterProtoAccessorTwoClasses(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#getterProtoAccessorTwoClasses

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getterProtoAccessorTwoClasses(Lookup
    #      *lookup, ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup29getterProtoAccessorTwoClassesEPS0_PNS_15Exec'
        'utionEngineERKNS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getterIndexed(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getterIndexed(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#getterIndexed

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getterIndexed(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup13getterIndexedEPS0_PNS_15ExecutionEngineERKNS'
        '_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getterQObject(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getterQObject(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#getterQObject

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getterQObject(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup13getterQObjectEPS0_PNS_15ExecutionEngineERKNS'
        '_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getterQObjectMethod(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getterQObjectMethod(Lookup
    *lookup, ExecutionEngine *engine, const Value &object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#getterQObjectMethod

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getterQObjectMethod(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup19getterQObjectMethodEPS0_PNS_15ExecutionEngin'
        'eERKNS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getterFallbackMethod(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getterFallbackMethod(Lookup
    *lookup, ExecutionEngine *engine, const Value &object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#getterFallbackMethod

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getterFallbackMethod(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup20getterFallbackMethodEPS0_PNS_15ExecutionEngi'
        'neERKNS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def getterValueType(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getterValueType(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#getterValueType

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getterValueType(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup15getterValueTypeEPS0_PNS_15ExecutionEngineERK'
        'NS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def primitiveGetterProto(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::primitiveGetterProto(Lookup
    *lookup, ExecutionEngine *engine, const Value &object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#primitiveGetterProto

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::primitiveGetterProto(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup20primitiveGetterProtoEPS0_PNS_15ExecutionEngi'
        'neERKNS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def primitiveGetterAccessor(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::primitiveGetterAccessor(Lookup
    *lookup, ExecutionEngine *engine, const Value &object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#primitiveGetterAccessor

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::primitiveGetterAccessor(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup23primitiveGetterAccessorEPS0_PNS_15ExecutionE'
        'ngineERKNS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(THIS, NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def stringLengthGetter(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::stringLengthGetter(Lookup *lookup,
    ExecutionEngine *engine, const Value &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#stringLengthGetter

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::stringLengthGetter(Lookup *lookup,
    #      ExecutionEngine *engine, const Value &object)
    return Rituals.call(
        'ritual_ZN3QV46Lookup18stringLengthGetterEPS0_PNS_15ExecutionEngine'
        'ERKNS_5ValueE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(object),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'])
  @overload(THIS, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'])
  @overload(NoneType, NoneType)
  def globalGetterGeneric(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::globalGetterGeneric(Lookup
    *lookup, ExecutionEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#globalGetterGeneric

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::Lookup::globalGetterGeneric(Lookup *lookup,
    #      ExecutionEngine *engine)
    return Rituals.call(
        'ritual_ZN3QV46Lookup19globalGetterGenericEPS0_PNS_15ExecutionEngin'
        'eE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'])
  @overload(THIS, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'])
  @overload(NoneType, NoneType)
  def globalGetterProto(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::globalGetterProto(Lookup *lookup,
    ExecutionEngine *engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#globalGetterProto

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::Lookup::globalGetterProto(Lookup *lookup,
    #      ExecutionEngine *engine)
    return Rituals.call(
        'ritual_ZN3QV46Lookup17globalGetterProtoEPS0_PNS_15ExecutionEngineE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'])
  @overload(THIS, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'])
  @overload(NoneType, NoneType)
  def globalGetterProtoAccessor(
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::globalGetterProtoAccessor(Lookup
    *lookup, ExecutionEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#globalGetterProtoAccessor

    Parameters
    ----------

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::Lookup::globalGetterProtoAccessor(Lookup *lookup,
    #      ExecutionEngine *engine)
    return Rituals.call(
        'ritual_ZN3QV46Lookup25globalGetterProtoAccessorEPS0_PNS_15Executio'
        'nEngineE',
        CuteMixin._addressOf(lookup), CuteMixin._addressOf(engine),
    )

  @staticmethod
  @overload(Call, THIS, WAIT['QV4.ExecutionEngine'])
  @overload(Call, THIS, NoneType)
  @overload(Call, NoneType, WAIT['QV4.ExecutionEngine'])
  @overload(Call, NoneType, NoneType)
  def doCallGlobal(
      call: Call,
      lookup: Optional[Lookup],
      engine: Optional[QV4.ExecutionEngine],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::doCallGlobal(Call call, Lookup
    *lookup, ExecutionEngine *engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#doCallGlobal

    Parameters
    ----------

    call : Call
      Passed on as its number.

    lookup : Optional[Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::Lookup::doCallGlobal(Call call, Lookup *lookup,
    #      ExecutionEngine *engine)
    return Rituals.call(
        'ritual_ZN3QV46Lookup12doCallGlobalENS0_4CallEPS0_PNS_15ExecutionEn'
        'gineE',
        call.value, CuteMixin._addressOf(lookup),
        CuteMixin._addressOf(engine),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Lookup'

  #  Qt's '~QV4::Lookup()'. Naming it makes this a value class: Python owns
  #  every C++ QV4::Lookup behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV46LookupD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Object'])
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, WAIT['QV4.Object'])
  @overload(NoneType, NoneType)
  def resolveGetter(
      self,
      engine: Optional[QV4.ExecutionEngine],
      object: Optional[QV4.Object],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::resolveGetter(ExecutionEngine
    *engine, const Object *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#resolveGetter

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::Lookup::resolveGetter(ExecutionEngine *engine,
    #      const Object *object)
    return self.uglySide.call(
        'ritual_ZN3QV46Lookup13resolveGetterEPNS_15ExecutionEngineEPKNS_6Ob'
        'jectE',
        self._addressOf(engine), self._addressOf(object),
    )

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.Value'])
  def resolvePrimitiveGetter(
      self,
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::Lookup::resolvePrimitiveGetter(ExecutionEngine *engine, const Value
    &object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#resolvePrimitiveGetter

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::resolvePrimitiveGetter(ExecutionEngine
    #      *engine, const Value &object)
    return self.uglySide.call(
        'ritual_ZN3QV46Lookup22resolvePrimitiveGetterEPNS_15ExecutionEngine'
        'ERKNS_5ValueE',
        self._addressOf(engine), self._valueOf(object),
    )

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def resolveGlobalGetter(
      self,
      engine: Optional[QV4.ExecutionEngine],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::Lookup::resolveGlobalGetter(ExecutionEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#resolveGlobalGetter

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::Lookup::resolveGlobalGetter(ExecutionEngine
    #      *engine)
    return self.uglySide.call(
        'ritual_ZN3QV46Lookup19resolveGlobalGetterEPNS_15ExecutionEngineE',
        self._addressOf(engine),
    )

  @overload(WAIT['QV4.PropertyKey'], WAIT['QV4.Heap.Object'])
  @overload(WAIT['QV4.PropertyKey'], NoneType)
  def resolveProtoGetter(
      self,
      name: QV4.PropertyKey,
      proto: Optional[QV4.Heap.Object],
  ) -> None:
    """
    Calls Qt's 'void QV4::Lookup::resolveProtoGetter(PropertyKey name, const
    Heap::Object *proto)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#resolveProtoGetter

    Parameters
    ----------

    name : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    proto : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Lookup::resolveProtoGetter(PropertyKey name, const
    #      Heap::Object *proto)
    self.uglySide.call(
        'ritual_ZN3QV46Lookup18resolveProtoGetterENS_11PropertyKeyEPKNS_4He'
        'ap6ObjectE',
        self._valueOf(name), self._addressOf(proto),
    )

  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Object'], WAIT['QV4.Value'],
  )
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.Object'], WAIT['QV4.Value'])
  @overload(NoneType, NoneType, WAIT['QV4.Value'])
  def resolveSetter(
      self,
      engine: Optional[QV4.ExecutionEngine],
      object: Optional[QV4.Object],
      value: QV4.Value,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Lookup::resolveSetter(ExecutionEngine *engine,
    Object *object, const Value &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#resolveSetter

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  bool QV4::Lookup::resolveSetter(ExecutionEngine *engine, Object
    #      *object, const Value &value)
    return self.uglySide.call(
        'ritual_ZN3QV46Lookup13resolveSetterEPNS_15ExecutionEngineEPNS_6Obj'
        'ectERKNS_5ValueE',
        self._addressOf(engine), self._addressOf(object),
        self._valueOf(value),
    )

  @overload(WAIT['QV4.MarkStack'])
  @overload(NoneType)
  def markObjects(self, stack: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QV4::Lookup::markObjects(MarkStack *stack)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#markObjects

    Parameters
    ----------

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Lookup::markObjects(MarkStack *stack)
    self.uglySide.call(
        'ritual_ZN3QV46Lookup11markObjectsEPNS_9MarkStackE',
        self._addressOf(stack),
    )

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, WAIT['QV4.Value'])
  @overload(NoneType, NoneType)
  def contextGetter(
      self,
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::contextGetter(ExecutionEngine
    *engine, Value *base)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#contextGetter

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::Lookup::contextGetter(ExecutionEngine *engine,
    #      Value *base)
    return self.uglySide.call(
        'ritual_ZN3QV46Lookup13contextGetterEPNS_15ExecutionEngineEPNS_5Val'
        'ueE',
        self._addressOf(engine), self._addressOf(base),
    )

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def globalGetter(self, engine: Optional[QV4.ExecutionEngine]) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::globalGetter(ExecutionEngine
    *engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#globalGetter

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::Lookup::globalGetter(ExecutionEngine *engine)
    return self.uglySide.call(
        'ritual_ZN3QV46Lookup12globalGetterEPNS_15ExecutionEngineE',
        self._addressOf(engine),
    )

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.Value'])
  def getter(
      self,
      engine: Optional[QV4.ExecutionEngine],
      object: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Lookup::getter(ExecutionEngine *engine,
    const Value &object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-lookup.html#getter

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Lookup::getter(ExecutionEngine *engine, const Value
    #      &object)
    return self.uglySide.call(
        'ritual_ZN3QV46Lookup6getterEPNS_15ExecutionEngineERKNS_5ValueE',
        self._addressOf(engine), self._valueOf(object),
    )

  def releasePropertyCache(self) -> None:
    """
    Calls Qt's 'void QV4::Lookup::releasePropertyCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-lookup.html#releasePropertyCache
    """
    #  void QV4::Lookup::releasePropertyCache()
    self.uglySide.call('ritual_ZN3QV46Lookup20releasePropertyCacheEv')

  @staticmethod
  def arrayLengthSetter(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Lookup::arrayLengthSetter(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Lookup.arrayLengthSetter' has no cute function yet. Qt's "
        "'bool QV4::Lookup::arrayLengthSetter(Lookup *lookup, "
        "ExecutionEngine *engine, Value &object, const Value &value)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setter(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Lookup::setter(ExecutionEngine *engine, Value &object,
    const Value &value)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Lookup.setter' has no cute function yet. Qt's 'bool "
        "QV4::Lookup::setter(ExecutionEngine *engine, Value &object, const "
        "Value &value)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setter0Inline(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Lookup::setter0Inline(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Lookup.setter0Inline' has no cute function yet. Qt's 'bool "
        "QV4::Lookup::setter0Inline(Lookup *lookup, ExecutionEngine "
        "*engine, Value &object, const Value &value)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def setter0MemberData(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Lookup::setter0MemberData(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Lookup.setter0MemberData' has no cute function yet. Qt's "
        "'bool QV4::Lookup::setter0MemberData(Lookup *lookup, "
        "ExecutionEngine *engine, Value &object, const Value &value)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setter0setter0(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Lookup::setter0setter0(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Lookup.setter0setter0' has no cute function yet. Qt's 'bool "
        "QV4::Lookup::setter0setter0(Lookup *lookup, ExecutionEngine "
        "*engine, Value &object, const Value &value)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def setterFallback(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Lookup::setterFallback(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Lookup.setterFallback' has no cute function yet. Qt's 'bool "
        "QV4::Lookup::setterFallback(Lookup *lookup, ExecutionEngine "
        "*engine, Value &object, const Value &value)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def setterGeneric(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Lookup::setterGeneric(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Lookup.setterGeneric' has no cute function yet. Qt's 'bool "
        "QV4::Lookup::setterGeneric(Lookup *lookup, ExecutionEngine "
        "*engine, Value &object, const Value &value)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def setterInsert(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Lookup::setterInsert(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Lookup.setterInsert' has no cute function yet. Qt's 'bool "
        "QV4::Lookup::setterInsert(Lookup *lookup, ExecutionEngine *engine, "
        "Value &object, const Value &value)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def setterQObject(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Lookup::setterQObject(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Lookup.setterQObject' has no cute function yet. Qt's 'bool "
        "QV4::Lookup::setterQObject(Lookup *lookup, ExecutionEngine "
        "*engine, Value &object, const Value &value)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def setterTwoClasses(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Lookup::setterTwoClasses(Lookup *lookup, ExecutionEngine
    *engine, Value &object, const Value &value)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Lookup.setterTwoClasses' has no cute function yet. Qt's 'bool "
        "QV4::Lookup::setterTwoClasses(Lookup *lookup, ExecutionEngine "
        "*engine, Value &object, const Value &value)': takes a type Python "
        "has no way to hand over yet.")
