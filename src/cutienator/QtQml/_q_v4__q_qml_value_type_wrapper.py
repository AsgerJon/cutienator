"""
QV4::QQmlValueTypeWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetypewrapper_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QV4::QQmlValueTypeWrapper to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMetaObject
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QObject, QVariant
  from . import QQmlPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlValueTypeWrapper(QV4.ReferenceObject):
  """
  The cute side of Qt's QV4::QQmlValueTypeWrapper: a plain Python object
  standing in front of one C++ QV4::QQmlValueTypeWrapper.

  It is built on the cute 'QV4::ReferenceObject', as Qt's
  QV4::QQmlValueTypeWrapper is built on Qt's QV4::ReferenceObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::QQmlValueTypeWrapper that has a ritual and that
  Python can call so far, 23 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultPrototype', 'virtualDestroy', 'create', 'toVariant', 'isEqual',
  'typeId', 'type', 'write', 'readReferenceValue', 'metaObject',
  'dataForPropertyKey', 'virtualPut', 'virtualIsEqualTo',
  'virtualHasProperty', 'virtualGetOwnProperty', 'method_toString',
  'virtualResolveLookupGetter', 'virtualResolveLookupSetter', 'initProto',
  'getGadgetProperty'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::QQmlValueTypeWrapper::staticVTable()':
    gives 'QV4::VTable', which has no cute class yet.
  - Qt's 'ReturnedValue QV4::QQmlValueTypeWrapper::create(ExecutionEngine
    *engine, const void *data, const QMetaObject *metaObject, QMetaType type,
    Heap::Object *object, int property, Heap::ReferenceObject::Flags flags)':
    names 'void', which has no cute class yet.
  - Qt's 'ReturnedValue QV4::QQmlValueTypeWrapper::create(ExecutionEngine
    *engine, const void *a1, const QMetaObject *metaObject, QMetaType type)':
    names 'void', which has no cute class yet.
  - Qt's 'bool QV4::QQmlValueTypeWrapper::toGadget(void *data) const': names
    'void', which has no cute class yet.
  - Qt's 'ReturnedValue QV4::QQmlValueTypeWrapper::virtualGet(const Managed
    *m, PropertyKey id, const Value *receiver, bool *hasProperty)': takes a
    number to change where it is.
  - Qt's 'OwnPropertyKeyIterator
    *QV4::QQmlValueTypeWrapper::virtualOwnPropertyKeys(const Object *m, Value
    *target)': gives 'QV4::OwnPropertyKeyIterator', which has no cute class
    yet.
  - Qt's 'int QV4::QQmlValueTypeWrapper::virtualMetacall(Object *object,
    QMetaObject::Call call, int index, void **a)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  5 of the 35 functions Qt declares: 3 forbidden; 1 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QV4::QQmlValueTypeWrapper is created at the first use, not by
    'QV4::QQmlValueTypeWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::QQmlValueTypeWrapper.
  - Each name of Qt's QV4::QQmlValueTypeWrapper that has no cute function
    yet, 'toGadget', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    *QV4::QQmlValueTypeWrapper::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#defaultPrototype

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
    #      *QV4::QQmlValueTypeWrapper::defaultPrototype(QV4::ExecutionEngine
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV420QQmlValueTypeWrapper16defaultPrototypeEPNS_15Execut'
        'ionEngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void
    QV4::QQmlValueTypeWrapper::virtualDestroy(QV4::Heap::Base *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QQmlValueTypeWrapper::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV420QQmlValueTypeWrapper14virtualDestroyEPNS_4Heap4Base'
        'E',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.QQmlValueTypeWrapper'],
      WAIT['QV4.Heap.Object'],
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.QQmlValueTypeWrapper'],
      NoneType,
  )
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, WAIT['QV4.Heap.Object'])
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, NoneType)
  @overload(
      NoneType, WAIT['QV4.Heap.QQmlValueTypeWrapper'],
      WAIT['QV4.Heap.Object'],
  )
  @overload(NoneType, WAIT['QV4.Heap.QQmlValueTypeWrapper'], NoneType)
  @overload(NoneType, NoneType, WAIT['QV4.Heap.Object'])
  @overload(NoneType, NoneType, NoneType)
  def create(
      engine: Optional[QV4.ExecutionEngine],
      cloneFrom: Optional[QV4.Heap.QQmlValueTypeWrapper],
      object: Optional[QV4.Heap.Object],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlValueTypeWrapper::create(ExecutionEngine *engine,
    Heap::QQmlValueTypeWrapper *cloneFrom, Heap::Object *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#create

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cloneFrom : Optional[QV4.Heap.QQmlValueTypeWrapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QQmlValueTypeWrapper::create(ExecutionEngine
    #      *engine, Heap::QQmlValueTypeWrapper *cloneFrom, Heap::Object
    #      *object)
    return Rituals.call(
        'ritual_ZN3QV420QQmlValueTypeWrapper6createEPNS_15ExecutionEngineEP'
        'NS_4Heap20QQmlValueTypeWrapperEPNS3_6ObjectE',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(cloneFrom),
        CuteMixin._addressOf(object),
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
    Calls Qt's 'bool QV4::QQmlValueTypeWrapper::virtualPut(Managed *m,
    PropertyKey id, const Value &value, Value *receiver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#virtualPut

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
    #  bool QV4::QQmlValueTypeWrapper::virtualPut(Managed *m, PropertyKey id,
    #      const Value &value, Value *receiver)
    return Rituals.call(
        'ritual_ZN3QV420QQmlValueTypeWrapper10virtualPutEPNS_7ManagedENS_11'
        'PropertyKeyERKNS_5ValueEPS4_',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._valueOf(value), CuteMixin._addressOf(receiver),
    )

  @staticmethod
  @overload(QV4.Managed, QV4.Managed)
  @overload(QV4.Managed, NoneType)
  @overload(NoneType, QV4.Managed)
  @overload(NoneType, NoneType)
  def virtualIsEqualTo(
      m: Optional[QV4.Managed],
      other: Optional[QV4.Managed],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::QQmlValueTypeWrapper::virtualIsEqualTo(Managed *m,
    Managed *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#virtualIsEqualTo

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    other : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::QQmlValueTypeWrapper::virtualIsEqualTo(Managed *m, Managed
    #      *other)
    return Rituals.call(
        'ritual_ZN3QV420QQmlValueTypeWrapper16virtualIsEqualToEPNS_7Managed'
        'ES2_',
        CuteMixin._addressOf(m), CuteMixin._addressOf(other),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'])
  @overload(NoneType, WAIT['QV4.PropertyKey'])
  def virtualHasProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::QQmlValueTypeWrapper::virtualHasProperty(const
    Managed *m, PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#virtualHasProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::QQmlValueTypeWrapper::virtualHasProperty(const Managed *m,
    #      PropertyKey id)
    return Rituals.call(
        'ritual_ZN3QV420QQmlValueTypeWrapper18virtualHasPropertyEPKNS_7Mana'
        'gedENS_11PropertyKeyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
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
    QV4::QQmlValueTypeWrapper::virtualGetOwnProperty(const Managed *m,
    PropertyKey id, Property *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html

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
    #  PropertyAttributes
    #      QV4::QQmlValueTypeWrapper::virtualGetOwnProperty(const Managed *m,
    #      PropertyKey id, Property *p)
    address = Rituals.call(
        'ritual_ZN3QV420QQmlValueTypeWrapper21virtualGetOwnPropertyEPKNS_7M'
        'anagedENS_11PropertyKeyEPNS_8PropertyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._addressOf(p),
    )
    return QV4.PropertyAttributes._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_toString(
      b: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlValueTypeWrapper::method_toString(const FunctionObject *b, const
    Value *thisObject, const Value *argv, int argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#method_toString

    Parameters
    ----------

    b : Optional[QV4.FunctionObject]
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
    #  ReturnedValue QV4::QQmlValueTypeWrapper::method_toString(const
    #      FunctionObject *b, const Value *thisObject, const Value *argv, int
    #      argc)
    return Rituals.call(
        'ritual_ZN3QV420QQmlValueTypeWrapper15method_toStringEPKNS_14Functi'
        'onObjectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(b), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
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
    QV4::QQmlValueTypeWrapper::virtualResolveLookupGetter(const Object
    *object, ExecutionEngine *engine, Lookup *lookup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html

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
    #  ReturnedValue
    #      QV4::QQmlValueTypeWrapper::virtualResolveLookupGetter(const Object
    #      *object, ExecutionEngine *engine, Lookup *lookup)
    return Rituals.call(
        'ritual_ZN3QV420QQmlValueTypeWrapper26virtualResolveLookupGetterEPK'
        'NS_6ObjectEPNS_15ExecutionEngineEPNS_6LookupE',
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
    Calls Qt's 'bool
    QV4::QQmlValueTypeWrapper::virtualResolveLookupSetter(Object *object,
    ExecutionEngine *engine, Lookup *lookup, const Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html

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
    #  bool QV4::QQmlValueTypeWrapper::virtualResolveLookupSetter(Object
    #      *object, ExecutionEngine *engine, Lookup *lookup, const Value
    #      &value)
    return Rituals.call(
        'ritual_ZN3QV420QQmlValueTypeWrapper26virtualResolveLookupSetterEPN'
        'S_6ObjectEPNS_15ExecutionEngineEPNS_6LookupERKNS_5ValueE',
        CuteMixin._addressOf(object), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(lookup), CuteMixin._valueOf(value),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def initProto(v4: Optional[QV4.ExecutionEngine]) -> None:
    """
    Calls Qt's 'void QV4::QQmlValueTypeWrapper::initProto(ExecutionEngine
    *v4)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#initProto

    Parameters
    ----------

    v4 : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QQmlValueTypeWrapper::initProto(ExecutionEngine *v4)
    Rituals.call(
        'ritual_ZN3QV420QQmlValueTypeWrapper9initProtoEPNS_15ExecutionEngin'
        'eE',
        CuteMixin._addressOf(v4),
    )

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.QQmlValueTypeWrapper'],
      QMetaType, int, bool, bool,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, QMetaType, int, bool, bool,
  )
  @overload(
      NoneType, WAIT['QV4.Heap.QQmlValueTypeWrapper'], QMetaType, int, bool,
      bool,
  )
  @overload(NoneType, NoneType, QMetaType, int, bool, bool)
  def getGadgetProperty(
      engine: Optional[QV4.ExecutionEngine],
      valueTypeWrapper: Optional[QV4.Heap.QQmlValueTypeWrapper],
      metaType: QMetaType,
      coreIndex: int,
      isFunction: bool,
      isEnum: bool,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlValueTypeWrapper::getGadgetProperty(ExecutionEngine *engine,
    Heap::QQmlValueTypeWrapper *valueTypeWrapper, QMetaType metaType, quint16
    coreIndex, bool isFunction, bool isEnum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#getGadgetProperty

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    valueTypeWrapper : Optional[QV4.Heap.QQmlValueTypeWrapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    coreIndex : int
      Passed on as it is.

    isFunction : bool
      Passed on as it is.

    isEnum : bool
      Passed on as it is.
    """
    #  ReturnedValue
    #      QV4::QQmlValueTypeWrapper::getGadgetProperty(ExecutionEngine
    #      *engine, Heap::QQmlValueTypeWrapper *valueTypeWrapper, QMetaType
    #      metaType, quint16 coreIndex, bool isFunction, bool isEnum)
    return Rituals.call(
        'ritual_ZN3QV420QQmlValueTypeWrapper17getGadgetPropertyEPNS_15Execu'
        'tionEngineEPNS_4Heap20QQmlValueTypeWrapperE9QMetaTypetbb',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(valueTypeWrapper),
        CuteMixin._valueOf(metaType), coreIndex, isFunction, isEnum,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::QQmlValueTypeWrapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.QQmlValueTypeWrapper]:
    """
    Calls Qt's 'QV4::Heap::QQmlValueTypeWrapper
    *QV4::QQmlValueTypeWrapper::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.QQmlValueTypeWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QQmlValueTypeWrapper
    #      *QV4::QQmlValueTypeWrapper::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV420QQmlValueTypeWrapper11d_uncheckedEv',
    )
    return QV4.Heap.QQmlValueTypeWrapper._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.QQmlValueTypeWrapper]:
    """
    Calls Qt's 'QV4::Heap::QQmlValueTypeWrapper
    *QV4::QQmlValueTypeWrapper::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#d

    Returns
    -------

    Optional[QV4.Heap.QQmlValueTypeWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QQmlValueTypeWrapper *QV4::QQmlValueTypeWrapper::d() const
    address = self.uglySide.call('ritual_ZNK3QV420QQmlValueTypeWrapper1dEv')
    return QV4.Heap.QQmlValueTypeWrapper._cuteAt(address)

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QV4::QQmlValueTypeWrapper::toVariant() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QV4::QQmlValueTypeWrapper::toVariant() const
    address = self.uglySide.call(
        'ritual_ZNK3QV420QQmlValueTypeWrapper9toVariantEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  def isEqual(self, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QV4::QQmlValueTypeWrapper::isEqual(const QVariant
    &value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#isEqual

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QV4::QQmlValueTypeWrapper::isEqual(const QVariant &value) const
    return self.uglySide.call(
        'ritual_ZNK3QV420QQmlValueTypeWrapper7isEqualERK8QVariant',
        self._valueOf(value),
    )

  def typeId(self) -> int:
    """
    Calls Qt's 'int QV4::QQmlValueTypeWrapper::typeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#typeId
    """
    #  int QV4::QQmlValueTypeWrapper::typeId() const
    return self.uglySide.call(
        'ritual_ZNK3QV420QQmlValueTypeWrapper6typeIdEv',
    )

  def type(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QV4::QQmlValueTypeWrapper::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#type

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QV4::QQmlValueTypeWrapper::type() const
    address = self.uglySide.call(
        'ritual_ZNK3QV420QQmlValueTypeWrapper4typeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  @overload(QObject, int)
  @overload(NoneType, int)
  def write(self, target: Optional[QObject], propertyIndex: int) -> bool:
    """
    Calls Qt's 'bool QV4::QQmlValueTypeWrapper::write(QObject *target, int
    propertyIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#write

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyIndex : int
      Passed on as it is.
    """
    #  bool QV4::QQmlValueTypeWrapper::write(QObject *target, int
    #      propertyIndex) const
    return self.uglySide.call(
        'ritual_ZNK3QV420QQmlValueTypeWrapper5writeEP7QObjecti',
        self._addressOf(target, 'QObject'), propertyIndex,
    )

  def readReferenceValue(self) -> bool:
    """
    Calls Qt's 'bool QV4::QQmlValueTypeWrapper::readReferenceValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#readReferenceValue
    """
    #  bool QV4::QQmlValueTypeWrapper::readReferenceValue() const
    return self.uglySide.call(
        'ritual_ZNK3QV420QQmlValueTypeWrapper18readReferenceValueEv',
    )

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QV4::QQmlValueTypeWrapper::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QV4::QQmlValueTypeWrapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV420QQmlValueTypeWrapper10metaObjectEv',
    )
    return QMetaObject._cuteAt(address)

  @overload(WAIT['QV4.PropertyKey'])
  def dataForPropertyKey(self, id: QV4.PropertyKey) -> QQmlPropertyData:
    """
    Calls Qt's 'QQmlPropertyData
    QV4::QQmlValueTypeWrapper::dataForPropertyKey(PropertyKey id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#dataForPropertyKey

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    Returns
    -------

    QQmlPropertyData
      A new cute QQmlPropertyData around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlPropertyData
    #      QV4::QQmlValueTypeWrapper::dataForPropertyKey(PropertyKey id)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV420QQmlValueTypeWrapper18dataForPropertyKeyENS_11Prop'
        'ertyKeyE',
        self._valueOf(id),
    )
    from . import QQmlPropertyData
    return QQmlPropertyData._cuteOwning(address)

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
    Calls Qt's 'void QV4::QQmlValueTypeWrapper::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlvaluetypewrapper.html#__dataTest
    """
    #  void QV4::QQmlValueTypeWrapper::__dataTest()
    self.uglySide.call('ritual_ZN3QV420QQmlValueTypeWrapper10__dataTestEv')

  @staticmethod
  def toGadget(*__, **_) -> Never:
    """
    Qt's 'bool QV4::QQmlValueTypeWrapper::toGadget(void *data) const': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.QQmlValueTypeWrapper.toGadget' has no cute function yet. Qt's "
        "'bool QV4::QQmlValueTypeWrapper::toGadget(void *data) const': "
        "names 'void', which has no cute class yet.")
