"""
QV4::QQmlTypeWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypewrapper_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::QQmlTypeWrapper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMetaObject
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QVariant
  from . import QQmlType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlType = WAIT['QQmlType']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTypeWrapper(QV4.FunctionObject):
  """
  The cute side of Qt's QV4::QQmlTypeWrapper: a plain Python object standing
  in front of one C++ QV4::QQmlTypeWrapper.

  It is built on the cute 'QV4::FunctionObject', as Qt's QV4::QQmlTypeWrapper
  is built on Qt's QV4::FunctionObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::QQmlTypeWrapper that has a ritual and that
  Python can call so far, 24 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultPrototype', 'virtualDestroy', 'isSingleton', 'metaObject',
  'object', 'singletonObject', 'toVariant', 'initProto', 'create',
  'virtualResolveLookupGetter', 'virtualResolveLookupSetter',
  'lookupSingletonProperty', 'lookupSingletonMethod', 'lookupEnumValue',
  'lookupEnum', 'virtualPut', 'virtualGetOwnProperty', 'virtualIsEqualTo',
  'virtualInstanceOf', 'method_hasInstance', 'method_toString'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::QQmlTypeWrapper::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'ReturnedValue QV4::QQmlTypeWrapper::create(ExecutionEngine *a0,
    QObject *a1, const QQmlRefPointer<QQmlTypeNameCache> &a2, const
    QQmlImportRef *a3, Heap::QQmlTypeWrapper::TypeNameMode a4)': takes a type
    Python has no way to hand over yet.
  - Qt's 'OwnPropertyKeyIterator
    *QV4::QQmlTypeWrapper::virtualOwnPropertyKeys(const Object *m, Value
    *target)': gives 'QV4::OwnPropertyKeyIterator', which has no cute class
    yet.
  - Qt's 'int QV4::QQmlTypeWrapper::virtualMetacall(Object *object,
    QMetaObject::Call call, int index, void **a)': takes a type Python has no
    way to hand over yet.
  - Qt's 'ReturnedValue QV4::QQmlTypeWrapper::virtualGet(const Managed *m,
    PropertyKey id, const Value *receiver, bool *hasProperty)': takes a
    number to change where it is.

  What has no ritual
  ------------------

  4 of the 33 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::QQmlTypeWrapper is created at the first use, not by
    'QV4::QQmlTypeWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::QQmlTypeWrapper.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::QQmlTypeWrapper::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#defaultPrototype

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Object
    #      *QV4::QQmlTypeWrapper::defaultPrototype(QV4::ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper16defaultPrototypeEPNS_15ExecutionEn'
        'gineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::QQmlTypeWrapper::virtualDestroy(QV4::Heap::Base
    *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QQmlTypeWrapper::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def initProto(v4: Optional[QV4.ExecutionEngine]) -> None:
    """
    Calls Qt's 'void QV4::QQmlTypeWrapper::initProto(ExecutionEngine *v4)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#initProto

    Parameters
    ----------

    v4 : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QQmlTypeWrapper::initProto(ExecutionEngine *v4)
    Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper9initProtoEPNS_15ExecutionEngineE',
        CuteMixin._addressOf(v4),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QObject, QQmlType)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, QQmlType)
  @overload(NoneType, QObject, QQmlType)
  @overload(NoneType, NoneType, QQmlType)
  @overload(
      WAIT['QV4.ExecutionEngine'], QObject, QQmlType,
      QV4.Heap.QQmlTypeWrapper.TypeNameMode,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, QQmlType,
      QV4.Heap.QQmlTypeWrapper.TypeNameMode,
  )
  @overload(
      NoneType, QObject, QQmlType, QV4.Heap.QQmlTypeWrapper.TypeNameMode,
  )
  @overload(
      NoneType, NoneType, QQmlType, QV4.Heap.QQmlTypeWrapper.TypeNameMode,
  )
  def create(
      a0: Optional[QV4.ExecutionEngine],
      a1: Optional[QObject],
      a2: QQmlType,
      a3: QV4.Heap.QQmlTypeWrapper.TypeNameMode = (
          QV4.Heap.QQmlTypeWrapper.TypeNameMode.IncludeEnums),
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QQmlTypeWrapper::create(ExecutionEngine
    *a0, QObject *a1, const QQmlType &a2, Heap::QQmlTypeWrapper::TypeNameMode
    a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#create

    Parameters
    ----------

    a0 : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : QQmlType
      Passed on as a value: Qt reads the C++ QQmlType, which stays Python's
      own.

    a3 : QV4.Heap.QQmlTypeWrapper.TypeNameMode
      Passed on as its number. May be left out, as in Qt: it is then
      QV4.Heap.QQmlTypeWrapper.TypeNameMode.IncludeEnums.
    """
    #  ReturnedValue QV4::QQmlTypeWrapper::create(ExecutionEngine *a0,
    #      QObject *a1, const QQmlType &a2,
    #      Heap::QQmlTypeWrapper::TypeNameMode a3)
    return Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper6createEPNS_15ExecutionEngineEP7QObj'
        'ectRK8QQmlTypeNS_4Heap15QQmlTypeWrapper12TypeNameModeE',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(a1, 'QObject'),
        CuteMixin._valueOf(a2), a3.value,
    )

  @staticmethod
  @overload(QV4.Object, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Lookup'])
  @overload(QV4.Object, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(QV4.Object, NoneType, WAIT['QV4.Lookup'])
  @overload(QV4.Object, NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Lookup'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, WAIT['QV4.Lookup'])
  @overload(NoneType, NoneType, NoneType)
  def virtualResolveLookupGetter(
      object: Optional[QV4.Object],
      engine: Optional[QV4.ExecutionEngine],
      lookup: Optional[QV4.Lookup],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlTypeWrapper::virtualResolveLookupGetter(const Object *object,
    ExecutionEngine *engine, Lookup *lookup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html

    Parameters
    ----------

    object : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lookup : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QQmlTypeWrapper::virtualResolveLookupGetter(const
    #      Object *object, ExecutionEngine *engine, Lookup *lookup)
    return Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper26virtualResolveLookupGetterEPKNS_6O'
        'bjectEPNS_15ExecutionEngineEPNS_6LookupE',
        CuteMixin._addressOf(object), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(lookup),
    )

  @staticmethod
  @overload(
      QV4.Object, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Lookup'], QV4.Value,
  )
  @overload(QV4.Object, WAIT['QV4.ExecutionEngine'], NoneType, QV4.Value)
  @overload(QV4.Object, NoneType, WAIT['QV4.Lookup'], QV4.Value)
  @overload(QV4.Object, NoneType, NoneType, QV4.Value)
  @overload(
      NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Lookup'], QV4.Value,
  )
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType, QV4.Value)
  @overload(NoneType, NoneType, WAIT['QV4.Lookup'], QV4.Value)
  @overload(NoneType, NoneType, NoneType, QV4.Value)
  def virtualResolveLookupSetter(
      object: Optional[QV4.Object],
      engine: Optional[QV4.ExecutionEngine],
      lookup: Optional[QV4.Lookup],
      value: QV4.Value,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::QQmlTypeWrapper::virtualResolveLookupSetter(Object
    *object, ExecutionEngine *engine, Lookup *lookup, const Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html

    Parameters
    ----------

    object : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lookup : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  bool QV4::QQmlTypeWrapper::virtualResolveLookupSetter(Object *object,
    #      ExecutionEngine *engine, Lookup *lookup, const Value &value)
    return Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper26virtualResolveLookupSetterEPNS_6Ob'
        'jectEPNS_15ExecutionEngineEPNS_6LookupERKNS_5ValueE',
        CuteMixin._addressOf(object), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(lookup), CuteMixin._valueOf(value),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, NoneType, QV4.Value)
  def lookupSingletonProperty(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlTypeWrapper::lookupSingletonProperty(Lookup *l, ExecutionEngine
    *engine, const Value &base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#lookupSingletonProperty

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::QQmlTypeWrapper::lookupSingletonProperty(Lookup *l,
    #      ExecutionEngine *engine, const Value &base)
    return Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper23lookupSingletonPropertyEPNS_6Looku'
        'pEPNS_15ExecutionEngineERKNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, NoneType, QV4.Value)
  def lookupSingletonMethod(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlTypeWrapper::lookupSingletonMethod(Lookup *l, ExecutionEngine
    *engine, const Value &base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#lookupSingletonMethod

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::QQmlTypeWrapper::lookupSingletonMethod(Lookup *l,
    #      ExecutionEngine *engine, const Value &base)
    return Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper21lookupSingletonMethodEPNS_6LookupE'
        'PNS_15ExecutionEngineERKNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, NoneType, QV4.Value)
  def lookupEnumValue(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QQmlTypeWrapper::lookupEnumValue(Lookup
    *l, ExecutionEngine *engine, const Value &base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#lookupEnumValue

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::QQmlTypeWrapper::lookupEnumValue(Lookup *l,
    #      ExecutionEngine *engine, const Value &base)
    return Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper15lookupEnumValueEPNS_6LookupEPNS_15'
        'ExecutionEngineERKNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, NoneType, QV4.Value)
  def lookupEnum(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QQmlTypeWrapper::lookupEnum(Lookup *l,
    ExecutionEngine *engine, const Value &base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#lookupEnum

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::QQmlTypeWrapper::lookupEnum(Lookup *l,
    #      ExecutionEngine *engine, const Value &base)
    return Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper10lookupEnumEPNS_6LookupEPNS_15Execu'
        'tionEngineERKNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._valueOf(base),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  @overload(NoneType, WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(NoneType, WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  def virtualPut(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
      value: QV4.Value,
      receiver: Optional[QV4.Value],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::QQmlTypeWrapper::virtualPut(Managed *m, PropertyKey
    id, const Value &value, Value *receiver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#virtualPut

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    receiver : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::QQmlTypeWrapper::virtualPut(Managed *m, PropertyKey id,
    #      const Value &value, Value *receiver)
    return Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper10virtualPutEPNS_7ManagedENS_11Prope'
        'rtyKeyERKNS_5ValueEPS4_',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._valueOf(value), CuteMixin._addressOf(receiver),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'])
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], NoneType)
  @overload(NoneType, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'])
  @overload(NoneType, WAIT['QV4.PropertyKey'], NoneType)
  def virtualGetOwnProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
      p: Optional[QV4.Property],
  ) -> QV4.PropertyAttributes:
    """
    Calls Qt's 'PropertyAttributes
    QV4::QQmlTypeWrapper::virtualGetOwnProperty(const Managed *m, PropertyKey
    id, Property *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#virtualGetOwnProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QV4.PropertyAttributes
      A new cute QV4::PropertyAttributes around the copy Qt gave back. Python
      owns it.
    """
    #  PropertyAttributes QV4::QQmlTypeWrapper::virtualGetOwnProperty(const
    #      Managed *m, PropertyKey id, Property *p)
    address = Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper21virtualGetOwnPropertyEPKNS_7Manage'
        'dENS_11PropertyKeyEPNS_8PropertyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._addressOf(p),
    )
    return QV4.PropertyAttributes._cuteOwning(address)

  @staticmethod
  @overload(QV4.Managed, QV4.Managed)
  @overload(QV4.Managed, NoneType)
  @overload(NoneType, QV4.Managed)
  @overload(NoneType, NoneType)
  def virtualIsEqualTo(
      that: Optional[QV4.Managed],
      o: Optional[QV4.Managed],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::QQmlTypeWrapper::virtualIsEqualTo(Managed *that,
    Managed *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#virtualIsEqualTo

    Parameters
    ----------

    that : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    o : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::QQmlTypeWrapper::virtualIsEqualTo(Managed *that, Managed *o)
    return Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper16virtualIsEqualToEPNS_7ManagedES2_',
        CuteMixin._addressOf(that), CuteMixin._addressOf(o),
    )

  @staticmethod
  @overload(QV4.Object, QV4.Value)
  @overload(NoneType, QV4.Value)
  def virtualInstanceOf(
      typeObject: Optional[QV4.Object],
      var: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QQmlTypeWrapper::virtualInstanceOf(const
    Object *typeObject, const Value &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#virtualInstanceOf

    Parameters
    ----------

    typeObject : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    var : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::QQmlTypeWrapper::virtualInstanceOf(const Object
    #      *typeObject, const Value &var)
    return Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper17virtualInstanceOfEPKNS_6ObjectERKN'
        'S_5ValueE',
        CuteMixin._addressOf(typeObject), CuteMixin._valueOf(var),
    )

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, QV4.Value, int)
  @overload(QV4.FunctionObject, QV4.Value, NoneType, int)
  @overload(QV4.FunctionObject, NoneType, QV4.Value, int)
  @overload(QV4.FunctionObject, NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_hasInstance(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QQmlTypeWrapper::method_hasInstance(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#method_hasInstance

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::QQmlTypeWrapper::method_hasInstance(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper18method_hasInstanceEPKNS_14Function'
        'ObjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(QV4.FunctionObject, QV4.Value, QV4.Value, int)
  @overload(QV4.FunctionObject, QV4.Value, NoneType, int)
  @overload(QV4.FunctionObject, NoneType, QV4.Value, int)
  @overload(QV4.FunctionObject, NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_toString(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      a2: Optional[QV4.Value],
      a3: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QQmlTypeWrapper::method_toString(const
    FunctionObject *b, const Value *thisObject, const Value *a2, int a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#method_toString

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a3 : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::QQmlTypeWrapper::method_toString(const
    #      FunctionObject *b, const Value *thisObject, const Value *a2, int
    #      a3)
    return Rituals.call(
        'ritual_ZN3QV415QQmlTypeWrapper15method_toStringEPKNS_14FunctionObj'
        'ectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(a2), a3,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::QQmlTypeWrapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.QQmlTypeWrapper]:
    """
    Calls Qt's 'QV4::Heap::QQmlTypeWrapper
    *QV4::QQmlTypeWrapper::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.QQmlTypeWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QQmlTypeWrapper *QV4::QQmlTypeWrapper::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415QQmlTypeWrapper11d_uncheckedEv',
    )
    return QV4.Heap.QQmlTypeWrapper._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.QQmlTypeWrapper]:
    """
    Calls Qt's 'QV4::Heap::QQmlTypeWrapper *QV4::QQmlTypeWrapper::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#d

    Returns
    -------

    Optional[QV4.Heap.QQmlTypeWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QQmlTypeWrapper *QV4::QQmlTypeWrapper::d() const
    address = self.uglySide.call('ritual_ZNK3QV415QQmlTypeWrapper1dEv')
    return QV4.Heap.QQmlTypeWrapper._cuteAt(address)

  def isSingleton(self) -> bool:
    """
    Calls Qt's 'bool QV4::QQmlTypeWrapper::isSingleton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#isSingleton
    """
    #  bool QV4::QQmlTypeWrapper::isSingleton() const
    return self.uglySide.call(
        'ritual_ZNK3QV415QQmlTypeWrapper11isSingletonEv',
    )

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QV4::QQmlTypeWrapper::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QV4::QQmlTypeWrapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415QQmlTypeWrapper10metaObjectEv',
    )
    return QMetaObject._cuteAt(address)

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QV4::QQmlTypeWrapper::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QV4::QQmlTypeWrapper::object() const
    address = self.uglySide.call('ritual_ZNK3QV415QQmlTypeWrapper6objectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def singletonObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QV4::QQmlTypeWrapper::singletonObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#singletonObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QV4::QQmlTypeWrapper::singletonObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415QQmlTypeWrapper15singletonObjectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QV4::QQmlTypeWrapper::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QV4::QQmlTypeWrapper::toVariant() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415QQmlTypeWrapper9toVariantEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::QQmlTypeWrapper::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmltypewrapper.html#__dataTest
    """
    #  void QV4::QQmlTypeWrapper::__dataTest()
    self.uglySide.call('ritual_ZN3QV415QQmlTypeWrapper10__dataTestEv')
