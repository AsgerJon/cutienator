"""
QV4::Object binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4object_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::Object to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QMetaObject
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Object(QV4.Managed):
  """
  The cute side of Qt's QV4::Object: a plain Python object standing in front
  of one C++ QV4::Object.

  It is built on the cute 'QV4::Managed', as Qt's QV4::Object is built on
  Qt's QV4::Managed, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Object that has a ritual and that Python can
  call so far, 72 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultInternalClass', 'defaultPrototype', 'setInternalClass',
  'propertyData', 'arrayData', 'setArrayData', 'getProperty', 'setProperty',
  'getOwnProperty', 'getValueOrSetter', 'hasProperty', 'defineOwnProperty',
  'getValue', 'getValueByIndex', 'getValueAccessor', 'putValue',
  'defineDefaultProperty', 'defineReadonlyProperty',
  'defineReadonlyConfigurableProperty', 'addSymbolSpecies', 'insertMember',
  'isExtensible', 'preventExtensions', 'getPrototypeOf', 'setPrototypeOf',
  'setPrototypeUnchecked', 'copyArrayData', 'setArrayLength',
  'setArrayLengthUnchecked', 'arraySet', 'arrayPut', 'setArrayAttributes',
  'push_back', 'setArrayType', 'arrayReserve', 'arrayCreate',
  'initSparseArray', 'sparseBegin', 'sparseEnd', 'protoHasArray', 'put',
  'putIndexed', 'setIndexed', 'set', 'deleteProperty', 'getLength',
  'instanceOf', 'isConcatSpreadable', 'isArray', 'setProtoFromNewTarget',
  'resolveLookupGetter', 'resolveLookupSetter', 'virtualPut',
  'virtualDeleteProperty', 'virtualHasProperty', 'virtualGetOwnProperty',
  'virtualDefineOwnProperty', 'virtualIsExtensible',
  'virtualPreventExtensions', 'virtualGetPrototypeOf',
  'virtualSetPrototypeOf', 'virtualGetLength', 'virtualInstanceOf',
  'virtualResolveLookupGetter', 'virtualResolveLookupSetter',
  'checkedInstanceOf', 'internalDefineOwnProperty', 'internalPut',
  'internalDeleteProperty'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::Object::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'const VTable *QV4::Object::vtable() const': gives 'QV4::VTable',
    which has no cute class yet.
  - Qt's 'void QV4::Object::defineDefaultProperty(const QString &name,
    VTable::Call code, int argumentCount, PropertyAttributes attributes)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QV4::Object::defineDefaultProperty(StringOrSymbol *name,
    VTable::Call code, int argumentCount, PropertyAttributes attributes)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QV4::Object::defineAccessorProperty(const QString &name,
    VTable::Call getter, VTable::Call setter)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QV4::Object::defineAccessorProperty(StringOrSymbol *name,
    VTable::Call getter, VTable::Call setter)': takes a type Python has no
    way to hand over yet.
  - Qt's 'ArrayData::Type QV4::Object::arrayType() const': gives a type
    Python has no way to take yet.
  - Qt's 'ReturnedValue QV4::Object::get(StringOrSymbol *name, bool
    *hasProperty, const Value *receiver) const': takes a number to change
    where it is.
  - Qt's 'ReturnedValue QV4::Object::get(uint idx, bool *hasProperty, const
    Value *receiver) const': takes a number to change where it is.
  - Qt's 'ReturnedValue QV4::Object::getIndexed(uint idx, bool *hasProperty)
    const': takes a number to change where it is.
  - Qt's 'ReturnedValue QV4::Object::get(PropertyKey id, const Value
    *receiver, bool *hasProperty) const': takes a number to change where it
    is.
  - Qt's 'OwnPropertyKeyIterator *QV4::Object::ownPropertyKeys(Value *target)
    const': gives 'QV4::OwnPropertyKeyIterator', which has no cute class yet.
  - Qt's 'const FunctionObject *QV4::Object::speciesConstructor(Scope &scope,
    const FunctionObject *defaultConstructor) const': takes a type Python has
    no way to hand over yet.
  - Qt's 'int QV4::Object::metacall(QMetaObject::Call call, int index, void
    **a)': takes a type Python has no way to hand over yet.
  - Qt's 'ReturnedValue QV4::Object::virtualGet(const Managed *m, PropertyKey
    id, const Value *receiver, bool *hasProperty)': takes a number to change
    where it is.
  - Qt's 'OwnPropertyKeyIterator *QV4::Object::virtualOwnPropertyKeys(const
    Object *m, Value *target)': gives 'QV4::OwnPropertyKeyIterator', which
    has no cute class yet.
  - Qt's 'int QV4::Object::virtualMetacall(Object *object, QMetaObject::Call
    call, int index, void **a)': takes a type Python has no way to hand over
    yet.
  - Qt's 'ReturnedValue QV4::Object::internalGet(PropertyKey id, const Value
    *receiver, bool *hasProperty) const': takes a number to change where it
    is.

  What has no ritual
  ------------------

  4 of the 107 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::Object is created at the first use, not by
    'QV4::Object(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Object.
  - Each name of Qt's QV4::Object that has no cute function yet, 'arrayType',
    'defineAccessorProperty', 'get', 'getIndexed', 'internalGet', 'metacall',
    'ownPropertyKeys', 'speciesConstructor', 'virtualGet', 'virtualMetacall',
    'virtualOwnPropertyKeys', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::Object, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ThrowOnFailure(CuteNum):
    """
    The enum 'QV4::Object::ThrowOnFailure' of Qt, with the 2 names Qt gives
    in it.
    """

    DoThrowOnRejection = Kee[int](0)
    DoNotThrow = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def defaultInternalClass(
      e: Optional[QV4.EngineBase],
  ) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass
    *QV4::Object::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#defaultInternalClass

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::InternalClass *QV4::Object::defaultInternalClass(QV4::EngineBase
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV46Object20defaultInternalClassEPNS_10EngineBaseE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(e: Optional[QV4.ExecutionEngine]) -> Optional[Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::Object::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#defaultPrototype

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Object *QV4::Object::defaultPrototype(QV4::ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV46Object16defaultPrototypeEPNS_15ExecutionEngineE',
        CuteMixin._addressOf(e),
    )
    return Object._cuteAt(address)

  @staticmethod
  @overload(QV4.Value, QV4.Value, WAIT['QV4.PropertyAttributes'])
  @overload(NoneType, QV4.Value, WAIT['QV4.PropertyAttributes'])
  def getValue(
      thisObject: Optional[QV4.Value],
      v: QV4.Value,
      attrs: QV4.PropertyAttributes,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Object::getValue(const Value *thisObject,
    const Value &v, PropertyAttributes attrs)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#getValue

    Parameters
    ----------

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    attrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  ReturnedValue QV4::Object::getValue(const Value *thisObject, const
    #      Value &v, PropertyAttributes attrs)
    return Rituals.call(
        'ritual_ZN3QV46Object8getValueEPKNS_5ValueERS2_NS_18PropertyAttribu'
        'tesE',
        CuteMixin._addressOf(thisObject), CuteMixin._valueOf(v),
        CuteMixin._valueOf(attrs),
    )

  @overload(QV4.Value, WAIT['QV4.PropertyAttributes'])
  def getValue(self, v: QV4.Value, attrs: QV4.PropertyAttributes) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Object::getValue(const Value &v,
    PropertyAttributes attrs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#getValue

    Parameters
    ----------

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    attrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  ReturnedValue QV4::Object::getValue(const Value &v, PropertyAttributes
    #      attrs) const
    return self.uglySide.call(
        'ritual_ZNK3QV46Object8getValueERKNS_5ValueENS_18PropertyAttributes'
        'E',
        self._valueOf(v), self._valueOf(attrs),
    )

  @staticmethod
  @overload(QV4.Value, QV4.Value, WAIT['QV4.PropertyAttributes'])
  @overload(NoneType, QV4.Value, WAIT['QV4.PropertyAttributes'])
  def getValueAccessor(
      thisObject: Optional[QV4.Value],
      v: QV4.Value,
      attrs: QV4.PropertyAttributes,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Object::getValueAccessor(const Value
    *thisObject, const Value &v, PropertyAttributes attrs)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#getValueAccessor

    Parameters
    ----------

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    attrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  ReturnedValue QV4::Object::getValueAccessor(const Value *thisObject,
    #      const Value &v, PropertyAttributes attrs)
    return Rituals.call(
        'ritual_ZN3QV46Object16getValueAccessorEPKNS_5ValueERS2_NS_18Proper'
        'tyAttributesE',
        CuteMixin._addressOf(thisObject), CuteMixin._valueOf(v),
        CuteMixin._valueOf(attrs),
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
    Calls Qt's 'bool QV4::Object::virtualPut(Managed *m, PropertyKey id,
    const Value &value, Value *receiver)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#virtualPut

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
    #  bool QV4::Object::virtualPut(Managed *m, PropertyKey id, const Value
    #      &value, Value *receiver)
    return Rituals.call(
        'ritual_ZN3QV46Object10virtualPutEPNS_7ManagedENS_11PropertyKeyERKN'
        'S_5ValueEPS4_',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._valueOf(value), CuteMixin._addressOf(receiver),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'])
  @overload(NoneType, WAIT['QV4.PropertyKey'])
  def virtualDeleteProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::virtualDeleteProperty(Managed *m,
    PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#virtualDeleteProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::Object::virtualDeleteProperty(Managed *m, PropertyKey id)
    return Rituals.call(
        'ritual_ZN3QV46Object21virtualDeletePropertyEPNS_7ManagedENS_11Prop'
        'ertyKeyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'])
  @overload(NoneType, WAIT['QV4.PropertyKey'])
  def virtualHasProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::virtualHasProperty(const Managed *m,
    PropertyKey id)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#virtualHasProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::Object::virtualHasProperty(const Managed *m, PropertyKey id)
    return Rituals.call(
        'ritual_ZN3QV46Object18virtualHasPropertyEPKNS_7ManagedENS_11Proper'
        'tyKeyE',
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
    Calls Qt's 'PropertyAttributes QV4::Object::virtualGetOwnProperty(const
    Managed *m, PropertyKey id, Property *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#virtualGetOwnProperty

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
    #  PropertyAttributes QV4::Object::virtualGetOwnProperty(const Managed
    #      *m, PropertyKey id, Property *p)
    address = Rituals.call(
        'ritual_ZN3QV46Object21virtualGetOwnPropertyEPKNS_7ManagedENS_11Pro'
        'pertyKeyEPNS_8PropertyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._addressOf(p),
    )
    return QV4.PropertyAttributes._cuteOwning(address)

  @staticmethod
  @overload(
      QV4.Managed, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      QV4.Managed, WAIT['QV4.PropertyKey'], NoneType,
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      NoneType, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      NoneType, WAIT['QV4.PropertyKey'], NoneType,
      WAIT['QV4.PropertyAttributes'],
  )
  def virtualDefineOwnProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
      p: Optional[QV4.Property],
      attrs: QV4.PropertyAttributes,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::virtualDefineOwnProperty(Managed *m,
    PropertyKey id, const Property *p, PropertyAttributes attrs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#virtualDefineOwnProperty

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

    attrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  bool QV4::Object::virtualDefineOwnProperty(Managed *m, PropertyKey id,
    #      const Property *p, PropertyAttributes attrs)
    return Rituals.call(
        'ritual_ZN3QV46Object24virtualDefineOwnPropertyEPNS_7ManagedENS_11P'
        'ropertyKeyEPKNS_8PropertyENS_18PropertyAttributesE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._addressOf(p), CuteMixin._valueOf(attrs),
    )

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualIsExtensible(m: Optional[QV4.Managed]) -> bool:
    """
    Calls Qt's 'bool QV4::Object::virtualIsExtensible(const Managed *m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#virtualIsExtensible

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Object::virtualIsExtensible(const Managed *m)
    return Rituals.call(
        'ritual_ZN3QV46Object19virtualIsExtensibleEPKNS_7ManagedE',
        CuteMixin._addressOf(m),
    )

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualPreventExtensions(a0: Optional[QV4.Managed]) -> bool:
    """
    Calls Qt's 'bool QV4::Object::virtualPreventExtensions(Managed *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#virtualPreventExtensions

    Parameters
    ----------

    a0 : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Object::virtualPreventExtensions(Managed *a0)
    return Rituals.call(
        'ritual_ZN3QV46Object24virtualPreventExtensionsEPNS_7ManagedE',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualGetPrototypeOf(
      a0: Optional[QV4.Managed],
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::Object::virtualGetPrototypeOf(const
    Managed *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#virtualGetPrototypeOf

    Parameters
    ----------

    a0 : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::Object::virtualGetPrototypeOf(const Managed *a0)
    address = Rituals.call(
        'ritual_ZN3QV46Object21virtualGetPrototypeOfEPKNS_7ManagedE',
        CuteMixin._addressOf(a0),
    )
    return QV4.Heap.Object._cuteAt(address)

  @staticmethod
  @overload(QV4.Managed, THIS)
  @overload(QV4.Managed, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def virtualSetPrototypeOf(
      a0: Optional[QV4.Managed],
      a1: Optional[Object],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::virtualSetPrototypeOf(Managed *a0, const
    Object *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#virtualSetPrototypeOf

    Parameters
    ----------

    a0 : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Object::virtualSetPrototypeOf(Managed *a0, const Object *a1)
    return Rituals.call(
        'ritual_ZN3QV46Object21virtualSetPrototypeOfEPNS_7ManagedEPKS0_',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(a1),
    )

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualGetLength(m: Optional[QV4.Managed]) -> int:
    """
    Calls Qt's 'qint64 QV4::Object::virtualGetLength(const Managed *m)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#virtualGetLength

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qint64 QV4::Object::virtualGetLength(const Managed *m)
    return Rituals.call(
        'ritual_ZN3QV46Object16virtualGetLengthEPKNS_7ManagedE',
        CuteMixin._addressOf(m),
    )

  @staticmethod
  @overload(THIS, QV4.Value)
  @overload(NoneType, QV4.Value)
  def virtualInstanceOf(typeObject: Optional[Object], var: QV4.Value) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Object::virtualInstanceOf(const Object
    *typeObject, const Value &var)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#virtualInstanceOf

    Parameters
    ----------

    typeObject : Optional[Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    var : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Object::virtualInstanceOf(const Object *typeObject,
    #      const Value &var)
    return Rituals.call(
        'ritual_ZN3QV46Object17virtualInstanceOfEPKS0_RKNS_5ValueE',
        CuteMixin._addressOf(typeObject), CuteMixin._valueOf(var),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Lookup'])
  @overload(THIS, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(THIS, NoneType, WAIT['QV4.Lookup'])
  @overload(THIS, NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Lookup'])
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, WAIT['QV4.Lookup'])
  @overload(NoneType, NoneType, NoneType)
  def virtualResolveLookupGetter(
      object: Optional[Object],
      engine: Optional[QV4.ExecutionEngine],
      lookup: Optional[QV4.Lookup],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Object::virtualResolveLookupGetter(const
    Object *object, ExecutionEngine *engine, Lookup *lookup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#virtualResolveLookupGetter

    Parameters
    ----------

    object : Optional[Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lookup : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::Object::virtualResolveLookupGetter(const Object
    #      *object, ExecutionEngine *engine, Lookup *lookup)
    return Rituals.call(
        'ritual_ZN3QV46Object26virtualResolveLookupGetterEPKS0_PNS_15Execut'
        'ionEngineEPNS_6LookupE',
        CuteMixin._addressOf(object), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(lookup),
    )

  @staticmethod
  @overload(THIS, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Lookup'], QV4.Value)
  @overload(THIS, WAIT['QV4.ExecutionEngine'], NoneType, QV4.Value)
  @overload(THIS, NoneType, WAIT['QV4.Lookup'], QV4.Value)
  @overload(THIS, NoneType, NoneType, QV4.Value)
  @overload(
      NoneType, WAIT['QV4.ExecutionEngine'], WAIT['QV4.Lookup'], QV4.Value,
  )
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType, QV4.Value)
  @overload(NoneType, NoneType, WAIT['QV4.Lookup'], QV4.Value)
  @overload(NoneType, NoneType, NoneType, QV4.Value)
  def virtualResolveLookupSetter(
      object: Optional[Object],
      engine: Optional[QV4.ExecutionEngine],
      lookup: Optional[QV4.Lookup],
      value: QV4.Value,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::virtualResolveLookupSetter(Object *object,
    ExecutionEngine *engine, Lookup *lookup, const Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#virtualResolveLookupSetter

    Parameters
    ----------

    object : Optional[Object]
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
    #  bool QV4::Object::virtualResolveLookupSetter(Object *object,
    #      ExecutionEngine *engine, Lookup *lookup, const Value &value)
    return Rituals.call(
        'ritual_ZN3QV46Object26virtualResolveLookupSetterEPS0_PNS_15Executi'
        'onEngineEPNS_6LookupERKNS_5ValueE',
        CuteMixin._addressOf(object), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(lookup), CuteMixin._valueOf(value),
    )

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.FunctionObject'], QV4.Value,
  )
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, QV4.Value)
  @overload(NoneType, WAIT['QV4.FunctionObject'], QV4.Value)
  @overload(NoneType, NoneType, QV4.Value)
  def checkedInstanceOf(
      engine: Optional[QV4.ExecutionEngine],
      typeObject: Optional[QV4.FunctionObject],
      var: QV4.Value,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Object::checkedInstanceOf(ExecutionEngine
    *engine, const FunctionObject *typeObject, const Value &var)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#checkedInstanceOf

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeObject : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    var : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Object::checkedInstanceOf(ExecutionEngine *engine,
    #      const FunctionObject *typeObject, const Value &var)
    return Rituals.call(
        'ritual_ZN3QV46Object17checkedInstanceOfEPNS_15ExecutionEngineEPKNS'
        '_14FunctionObjectERKNS_5ValueE',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(typeObject),
        CuteMixin._valueOf(var),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Object'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'QV4::Heap::Object *QV4::Object::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Object *QV4::Object::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV46Object11d_uncheckedEv')
    return QV4.Heap.Object._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'QV4::Heap::Object *QV4::Object::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#d

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Object *QV4::Object::d() const
    address = self.uglySide.call('ritual_ZNK3QV46Object1dEv')
    return QV4.Heap.Object._cuteAt(address)

  @overload(int)
  def propertyData(self, index: int) -> Optional[QV4.Value]:
    """
    Calls Qt's 'const Value *QV4::Object::propertyData(uint index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#propertyData

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Value *QV4::Object::propertyData(uint index) const
    address = self.uglySide.call(
        'ritual_ZNK3QV46Object12propertyDataEj', index,
    )
    return QV4.Value._cuteAt(address)

  def arrayData(self) -> Optional[QV4.Heap.ArrayData]:
    """
    Calls Qt's 'Heap::ArrayData *QV4::Object::arrayData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#arrayData

    Returns
    -------

    Optional[QV4.Heap.ArrayData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::ArrayData *QV4::Object::arrayData() const
    address = self.uglySide.call('ritual_ZNK3QV46Object9arrayDataEv')
    return QV4.Heap.ArrayData._cuteAt(address)

  @overload(WAIT['QV4.PropertyKey'])
  @overload(WAIT['QV4.PropertyKey'], WAIT['QV4.Property'])
  @overload(WAIT['QV4.PropertyKey'], NoneType)
  def getOwnProperty(
      self,
      id: QV4.PropertyKey,
      p: Optional[QV4.Property] = None,
  ) -> QV4.PropertyAttributes:
    """
    Calls Qt's 'PropertyAttributes QV4::Object::getOwnProperty(PropertyKey
    id, Property *p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#getOwnProperty

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QV4.PropertyAttributes
      A new cute QV4::PropertyAttributes around the copy Qt gave back. Python
      owns it.
    """
    #  PropertyAttributes QV4::Object::getOwnProperty(PropertyKey id,
    #      Property *p) const
    address = self.uglySide.call(
        'ritual_ZNK3QV46Object14getOwnPropertyENS_11PropertyKeyEPNS_8Proper'
        'tyE',
        self._valueOf(id), self._addressOf(p),
    )
    return QV4.PropertyAttributes._cuteOwning(address)

  @overload(WAIT['QV4.PropertyKey'])
  def hasProperty(self, id: QV4.PropertyKey) -> bool:
    """
    Calls Qt's 'bool QV4::Object::hasProperty(PropertyKey id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#hasProperty

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::Object::hasProperty(PropertyKey id) const
    return self.uglySide.call(
        'ritual_ZNK3QV46Object11hasPropertyENS_11PropertyKeyE',
        self._valueOf(id),
    )

  @overload(int)
  def getValueByIndex(self, propertyIndex: int) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Object::getValueByIndex(uint
    propertyIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#getValueByIndex

    Parameters
    ----------

    propertyIndex : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::Object::getValueByIndex(uint propertyIndex) const
    return self.uglySide.call(
        'ritual_ZNK3QV46Object15getValueByIndexEj', propertyIndex,
    )

  def isExtensible(self) -> bool:
    """
    Calls Qt's 'bool QV4::Object::isExtensible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#isExtensible
    """
    #  bool QV4::Object::isExtensible() const
    return self.uglySide.call('ritual_ZNK3QV46Object12isExtensibleEv')

  def getPrototypeOf(self) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::Object::getPrototypeOf() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#getPrototypeOf

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::Object::getPrototypeOf() const
    address = self.uglySide.call('ritual_ZNK3QV46Object14getPrototypeOfEv')
    return QV4.Heap.Object._cuteAt(address)

  def sparseBegin(self) -> Optional[QV4.SparseArrayNode]:
    """
    Calls Qt's 'SparseArrayNode *QV4::Object::sparseBegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#sparseBegin

    Returns
    -------

    Optional[QV4.SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArrayNode *QV4::Object::sparseBegin() const
    address = self.uglySide.call('ritual_ZNK3QV46Object11sparseBeginEv')
    return QV4.SparseArrayNode._cuteAt(address)

  def sparseEnd(self) -> Optional[QV4.SparseArrayNode]:
    """
    Calls Qt's 'SparseArrayNode *QV4::Object::sparseEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#sparseEnd

    Returns
    -------

    Optional[QV4.SparseArrayNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArrayNode *QV4::Object::sparseEnd() const
    address = self.uglySide.call('ritual_ZNK3QV46Object9sparseEndEv')
    return QV4.SparseArrayNode._cuteAt(address)

  def getLength(self) -> int:
    """
    Calls Qt's 'qint64 QV4::Object::getLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#getLength
    """
    #  qint64 QV4::Object::getLength() const
    return self.uglySide.call('ritual_ZNK3QV46Object9getLengthEv')

  @overload(QV4.Value)
  def instanceOf(self, var: QV4.Value) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Object::instanceOf(const Value &var)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#instanceOf

    Parameters
    ----------

    var : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::Object::instanceOf(const Value &var) const
    return self.uglySide.call(
        'ritual_ZNK3QV46Object10instanceOfERKNS_5ValueE', self._valueOf(var),
    )

  def isConcatSpreadable(self) -> bool:
    """
    Calls Qt's 'bool QV4::Object::isConcatSpreadable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#isConcatSpreadable
    """
    #  bool QV4::Object::isConcatSpreadable() const
    return self.uglySide.call('ritual_ZNK3QV46Object18isConcatSpreadableEv')

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QV4::Object::isArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#isArray
    """
    #  bool QV4::Object::isArray() const
    return self.uglySide.call('ritual_ZNK3QV46Object7isArrayEv')

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Lookup'])
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, WAIT['QV4.Lookup'])
  @overload(NoneType, NoneType)
  def resolveLookupGetter(
      self,
      engine: Optional[QV4.ExecutionEngine],
      lookup: Optional[QV4.Lookup],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::Object::resolveLookupGetter(ExecutionEngine *engine, Lookup *lookup)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#resolveLookupGetter

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lookup : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::Object::resolveLookupGetter(ExecutionEngine
    #      *engine, Lookup *lookup) const
    return self.uglySide.call(
        'ritual_ZNK3QV46Object19resolveLookupGetterEPNS_15ExecutionEngineEP'
        'NS_6LookupE',
        self._addressOf(engine), self._addressOf(lookup),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.Heap.InternalClass'])
  @overload(NoneType)
  def setInternalClass(self, ic: Optional[QV4.Heap.InternalClass]) -> None:
    """
    Calls Qt's 'void QV4::Object::setInternalClass(Heap::InternalClass *ic)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#setInternalClass

    Parameters
    ----------

    ic : Optional[QV4.Heap.InternalClass]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Object::setInternalClass(Heap::InternalClass *ic)
    self.uglySide.call(
        'ritual_ZN3QV46Object16setInternalClassEPNS_4Heap13InternalClassE',
        self._addressOf(ic),
    )

  @overload(WAIT['QV4.ArrayData'])
  @overload(NoneType)
  def setArrayData(self, a: Optional[QV4.ArrayData]) -> None:
    """
    Calls Qt's 'void QV4::Object::setArrayData(ArrayData *a)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#setArrayData

    Parameters
    ----------

    a : Optional[QV4.ArrayData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Object::setArrayData(ArrayData *a)
    self.uglySide.call(
        'ritual_ZN3QV46Object12setArrayDataEPNS_9ArrayDataE',
        self._addressOf(a),
    )

  @overload(WAIT['QV4.InternalClassEntry'], WAIT['QV4.Property'])
  @overload(WAIT['QV4.InternalClassEntry'], NoneType)
  def setProperty(
      self,
      entry: QV4.InternalClassEntry,
      p: Optional[QV4.Property],
  ) -> None:
    """
    Calls Qt's 'void QV4::Object::setProperty(const InternalClassEntry
    &entry, const Property *p)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#setProperty

    Parameters
    ----------

    entry : QV4.InternalClassEntry
      Passed on as a value: Qt reads the C++ QV4::InternalClassEntry, which
      stays Python's own.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Object::setProperty(const InternalClassEntry &entry, const
    #      Property *p)
    self.uglySide.call(
        'ritual_ZN3QV46Object11setPropertyERKNS_18InternalClassEntryEPKNS_8'
        'PropertyE',
        self._valueOf(entry), self._addressOf(p),
    )

  @overload(int, QV4.Value)
  def setProperty(self, index: int, v: QV4.Value) -> None:
    """
    Calls Qt's 'void QV4::Object::setProperty(uint index, Value v) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#setProperty

    Parameters
    ----------

    index : int
      Passed on as it is.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::Object::setProperty(uint index, Value v) const
    self.uglySide.call(
        'ritual_ZNK3QV46Object11setPropertyEjNS_5ValueE',
        index, self._valueOf(v),
    )

  @overload(int, WAIT['QV4.Heap.Base'])
  @overload(int, NoneType)
  def setProperty(self, index: int, b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::Object::setProperty(uint index, Heap::Base *b)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#setProperty

    Parameters
    ----------

    index : int
      Passed on as it is.

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Object::setProperty(uint index, Heap::Base *b) const
    self.uglySide.call(
        'ritual_ZNK3QV46Object11setPropertyEjPNS_4Heap4BaseE',
        index, self._addressOf(b),
    )

  @overload(WAIT['QV4.ExecutionEngine'], int, QV4.Value)
  @overload(NoneType, int, QV4.Value)
  def setProperty(
      self,
      engine: Optional[QV4.ExecutionEngine],
      index: int,
      v: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QV4::Object::setProperty(ExecutionEngine *engine, uint
    index, Value v) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#setProperty

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::Object::setProperty(ExecutionEngine *engine, uint index,
    #      Value v) const
    self.uglySide.call(
        'ritual_ZNK3QV46Object11setPropertyEPNS_15ExecutionEngineEjNS_5Valu'
        'eE',
        self._addressOf(engine), index, self._valueOf(v),
    )

  @overload(WAIT['QV4.ExecutionEngine'], int, WAIT['QV4.Heap.Base'])
  @overload(WAIT['QV4.ExecutionEngine'], int, NoneType)
  @overload(NoneType, int, WAIT['QV4.Heap.Base'])
  @overload(NoneType, int, NoneType)
  def setProperty(
      self,
      engine: Optional[QV4.ExecutionEngine],
      index: int,
      b: Optional[QV4.Heap.Base],
  ) -> None:
    """
    Calls Qt's 'void QV4::Object::setProperty(ExecutionEngine *engine, uint
    index, Heap::Base *b) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#setProperty

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Object::setProperty(ExecutionEngine *engine, uint index,
    #      Heap::Base *b) const
    self.uglySide.call(
        'ritual_ZNK3QV46Object11setPropertyEPNS_15ExecutionEngineEjPNS_4Hea'
        'p4BaseE',
        self._addressOf(engine), index, self._addressOf(b),
    )

  @overload(THIS)
  @overload(NoneType)
  def setPrototypeOf(self, p: Optional[Object]) -> bool:
    """
    Calls Qt's 'bool QV4::Object::setPrototypeOf(const Object *p)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#setPrototypeOf

    Parameters
    ----------

    p : Optional[Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Object::setPrototypeOf(const Object *p)
    return self.uglySide.call(
        'ritual_ZN3QV46Object14setPrototypeOfEPKS0_', self._addressOf(p),
    )

  @overload(THIS)
  @overload(NoneType)
  def setPrototypeUnchecked(self, p: Optional[Object]) -> None:
    """
    Calls Qt's 'void QV4::Object::setPrototypeUnchecked(const Object *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#setPrototypeUnchecked

    Parameters
    ----------

    p : Optional[Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Object::setPrototypeUnchecked(const Object *p)
    self.uglySide.call(
        'ritual_ZN3QV46Object21setPrototypeUncheckedEPKS0_',
        self._addressOf(p),
    )

  @overload(int)
  def setArrayLength(self, newLen: int) -> bool:
    """
    Calls Qt's 'bool QV4::Object::setArrayLength(uint newLen)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#setArrayLength

    Parameters
    ----------

    newLen : int
      Passed on as it is.
    """
    #  bool QV4::Object::setArrayLength(uint newLen)
    return self.uglySide.call(
        'ritual_ZN3QV46Object14setArrayLengthEj', newLen,
    )

  @overload(int)
  def setArrayLengthUnchecked(self, l: int) -> None:
    """
    Calls Qt's 'void QV4::Object::setArrayLengthUnchecked(uint l)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#setArrayLengthUnchecked

    Parameters
    ----------

    l : int
      Passed on as it is.
    """
    #  void QV4::Object::setArrayLengthUnchecked(uint l)
    self.uglySide.call('ritual_ZN3QV46Object23setArrayLengthUncheckedEj', l)

  @overload(int, WAIT['QV4.PropertyAttributes'])
  def setArrayAttributes(self, i: int, a: QV4.PropertyAttributes) -> None:
    """
    Calls Qt's 'void QV4::Object::setArrayAttributes(uint i,
    PropertyAttributes a)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#setArrayAttributes

    Parameters
    ----------

    i : int
      Passed on as it is.

    a : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  void QV4::Object::setArrayAttributes(uint i, PropertyAttributes a)
    self.uglySide.call(
        'ritual_ZN3QV46Object18setArrayAttributesEjNS_18PropertyAttributesE',
        i, self._valueOf(a),
    )

  @overload(QV4.Heap.ArrayData.Type)
  def setArrayType(self, t: QV4.Heap.ArrayData.Type) -> None:
    """
    Calls Qt's 'void QV4::Object::setArrayType(ArrayData::Type t)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#setArrayType

    Parameters
    ----------

    t : QV4.Heap.ArrayData.Type
      Passed on as its number.
    """
    #  void QV4::Object::setArrayType(ArrayData::Type t)
    self.uglySide.call(
        'ritual_ZN3QV46Object12setArrayTypeENS_4Heap9ArrayData4TypeE',
        t.value,
    )

  @overload(int, QV4.Value, ThrowOnFailure)
  def setIndexed(
      self,
      idx: int,
      v: QV4.Value,
      shouldThrow: ThrowOnFailure,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::setIndexed(uint idx, const Value &v,
    ThrowOnFailure shouldThrow)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#setIndexed

    Parameters
    ----------

    idx : int
      Passed on as it is.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    shouldThrow : ThrowOnFailure
      Passed on as its number.
    """
    #  bool QV4::Object::setIndexed(uint idx, const Value &v, ThrowOnFailure
    #      shouldThrow)
    return self.uglySide.call(
        'ritual_ZN3QV46Object10setIndexedEjRKNS_5ValueENS0_14ThrowOnFailure'
        'E',
        idx, self._valueOf(v), shouldThrow.value,
    )

  @overload(QV4.Value)
  @overload(NoneType)
  def setProtoFromNewTarget(self, newTarget: Optional[QV4.Value]) -> bool:
    """
    Calls Qt's 'bool QV4::Object::setProtoFromNewTarget(const Value
    *newTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#setProtoFromNewTarget

    Parameters
    ----------

    newTarget : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Object::setProtoFromNewTarget(const Value *newTarget)
    return self.uglySide.call(
        'ritual_ZN3QV46Object21setProtoFromNewTargetEPKNS_5ValueE',
        self._addressOf(newTarget),
    )

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
    Calls Qt's 'void QV4::Object::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#__dataTest
    """
    #  void QV4::Object::__dataTest()
    self.uglySide.call('ritual_ZN3QV46Object10__dataTestEv')

  @overload(WAIT['QV4.InternalClassEntry'], WAIT['QV4.Property'])
  @overload(WAIT['QV4.InternalClassEntry'], NoneType)
  def getProperty(
      self,
      entry: QV4.InternalClassEntry,
      p: Optional[QV4.Property],
  ) -> None:
    """
    Calls Qt's 'void QV4::Object::getProperty(const InternalClassEntry
    &entry, Property *p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#getProperty

    Parameters
    ----------

    entry : QV4.InternalClassEntry
      Passed on as a value: Qt reads the C++ QV4::InternalClassEntry, which
      stays Python's own.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Object::getProperty(const InternalClassEntry &entry,
    #      Property *p) const
    self.uglySide.call(
        'ritual_ZNK3QV46Object11getPropertyERKNS_18InternalClassEntryEPNS_8'
        'PropertyE',
        self._valueOf(entry), self._addressOf(p),
    )

  @overload(WAIT['QV4.PropertyKey'], WAIT['QV4.PropertyAttributes'])
  @overload(WAIT['QV4.PropertyKey'], NoneType)
  def getValueOrSetter(
      self,
      id: QV4.PropertyKey,
      attrs: Optional[QV4.PropertyAttributes],
  ) -> QV4.PropertyIndex:
    """
    Calls Qt's 'PropertyIndex QV4::Object::getValueOrSetter(PropertyKey id,
    PropertyAttributes *attrs)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#getValueOrSetter

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    attrs : Optional[QV4.PropertyAttributes]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QV4.PropertyIndex
      A new cute QV4::PropertyIndex around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyIndex QV4::Object::getValueOrSetter(PropertyKey id,
    #      PropertyAttributes *attrs)
    address = self.uglySide.call(
        'ritual_ZN3QV46Object16getValueOrSetterENS_11PropertyKeyEPNS_18Prop'
        'ertyAttributesE',
        self._valueOf(id), self._addressOf(attrs),
    )
    return QV4.PropertyIndex._cuteOwning(address)

  @overload(
      WAIT['QV4.PropertyKey'], WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      WAIT['QV4.PropertyKey'], NoneType, WAIT['QV4.PropertyAttributes'],
  )
  def defineOwnProperty(
      self,
      id: QV4.PropertyKey,
      p: Optional[QV4.Property],
      attrs: QV4.PropertyAttributes,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::defineOwnProperty(PropertyKey id, const
    Property *p, PropertyAttributes attrs)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#defineOwnProperty

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  bool QV4::Object::defineOwnProperty(PropertyKey id, const Property *p,
    #      PropertyAttributes attrs)
    return self.uglySide.call(
        'ritual_ZN3QV46Object17defineOwnPropertyENS_11PropertyKeyEPKNS_8Pro'
        'pertyENS_18PropertyAttributesE',
        self._valueOf(id), self._addressOf(p), self._valueOf(attrs),
    )

  @overload(int, WAIT['QV4.PropertyAttributes'], QV4.Value)
  def putValue(
      self,
      memberIndex: int,
      attrs: QV4.PropertyAttributes,
      value: QV4.Value,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::putValue(uint memberIndex,
    PropertyAttributes attrs, const Value &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#putValue

    Parameters
    ----------

    memberIndex : int
      Passed on as it is.

    attrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  bool QV4::Object::putValue(uint memberIndex, PropertyAttributes attrs,
    #      const Value &value)
    return self.uglySide.call(
        'ritual_ZN3QV46Object8putValueEjNS_18PropertyAttributesERKNS_5Value'
        'E',
        memberIndex, self._valueOf(attrs), self._valueOf(value),
    )

  @overload(
      WAIT['QV4.StringOrSymbol'], QV4.Value, WAIT['QV4.PropertyAttributes'],
  )
  @overload(NoneType, QV4.Value, WAIT['QV4.PropertyAttributes'])
  def defineDefaultProperty(
      self,
      name: Optional[QV4.StringOrSymbol],
      value: QV4.Value,
      attributes: QV4.PropertyAttributes,
  ) -> None:
    """
    Calls Qt's 'void QV4::Object::defineDefaultProperty(StringOrSymbol *name,
    const Value &value, PropertyAttributes attributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#defineDefaultProperty

    Parameters
    ----------

    name : Optional[QV4.StringOrSymbol]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    attributes : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  void QV4::Object::defineDefaultProperty(StringOrSymbol *name, const
    #      Value &value, PropertyAttributes attributes)
    self.uglySide.call(
        'ritual_ZN3QV46Object21defineDefaultPropertyEPNS_14StringOrSymbolER'
        'KNS_5ValueENS_18PropertyAttributesE',
        self._addressOf(name), self._valueOf(value),
        self._valueOf(attributes),
    )

  @overload(str, QV4.Value, WAIT['QV4.PropertyAttributes'])
  def defineDefaultProperty(
      self,
      name: str,
      value: QV4.Value,
      attributes: QV4.PropertyAttributes,
  ) -> None:
    """
    Calls Qt's 'void QV4::Object::defineDefaultProperty(const QString &name,
    const Value &value, PropertyAttributes attributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#defineDefaultProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    attributes : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  void QV4::Object::defineDefaultProperty(const QString &name, const
    #      Value &value, PropertyAttributes attributes)
    self.uglySide.call(
        'ritual_ZN3QV46Object21defineDefaultPropertyERK7QStringRKNS_5ValueE'
        'NS_18PropertyAttributesE',
        name, self._valueOf(value), self._valueOf(attributes),
    )

  @overload(str, QV4.Value)
  def defineReadonlyProperty(self, name: str, value: QV4.Value) -> None:
    """
    Calls Qt's 'void QV4::Object::defineReadonlyProperty(const QString &name,
    const Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#defineReadonlyProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::Object::defineReadonlyProperty(const QString &name, const
    #      Value &value)
    self.uglySide.call(
        'ritual_ZN3QV46Object22defineReadonlyPropertyERK7QStringRKNS_5Value'
        'E',
        name, self._valueOf(value),
    )

  @overload(WAIT['QV4.String'], QV4.Value)
  @overload(NoneType, QV4.Value)
  def defineReadonlyProperty(
      self,
      name: Optional[QV4.String],
      value: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QV4::Object::defineReadonlyProperty(String *name, const
    Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#defineReadonlyProperty

    Parameters
    ----------

    name : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::Object::defineReadonlyProperty(String *name, const Value
    #      &value)
    self.uglySide.call(
        'ritual_ZN3QV46Object22defineReadonlyPropertyEPNS_6StringERKNS_5Val'
        'ueE',
        self._addressOf(name), self._valueOf(value),
    )

  @overload(str, QV4.Value)
  def defineReadonlyConfigurableProperty(
      self,
      name: str,
      value: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QV4::Object::defineReadonlyConfigurableProperty(const
    QString &name, const Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#defineReadonlyConfigurableProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::Object::defineReadonlyConfigurableProperty(const QString
    #      &name, const Value &value)
    self.uglySide.call(
        'ritual_ZN3QV46Object34defineReadonlyConfigurablePropertyERK7QStrin'
        'gRKNS_5ValueE',
        name, self._valueOf(value),
    )

  @overload(WAIT['QV4.StringOrSymbol'], QV4.Value)
  @overload(NoneType, QV4.Value)
  def defineReadonlyConfigurableProperty(
      self,
      name: Optional[QV4.StringOrSymbol],
      value: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Object::defineReadonlyConfigurableProperty(StringOrSymbol *name,
    const Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#defineReadonlyConfigurableProperty

    Parameters
    ----------

    name : Optional[QV4.StringOrSymbol]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::Object::defineReadonlyConfigurableProperty(StringOrSymbol
    #      *name, const Value &value)
    self.uglySide.call(
        'ritual_ZN3QV46Object34defineReadonlyConfigurablePropertyEPNS_14Str'
        'ingOrSymbolERKNS_5ValueE',
        self._addressOf(name), self._valueOf(value),
    )

  def addSymbolSpecies(self) -> None:
    """
    Calls Qt's 'void QV4::Object::addSymbolSpecies()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#addSymbolSpecies
    """
    #  void QV4::Object::addSymbolSpecies()
    self.uglySide.call('ritual_ZN3QV46Object16addSymbolSpeciesEv')

  @overload(
      WAIT['QV4.StringOrSymbol'], QV4.Value, WAIT['QV4.PropertyAttributes'],
  )
  @overload(NoneType, QV4.Value, WAIT['QV4.PropertyAttributes'])
  def insertMember(
      self,
      s: Optional[QV4.StringOrSymbol],
      v: QV4.Value,
      attributes: QV4.PropertyAttributes,
  ) -> None:
    """
    Calls Qt's 'void QV4::Object::insertMember(StringOrSymbol *s, const Value
    &v, PropertyAttributes attributes)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#insertMember

    Parameters
    ----------

    s : Optional[QV4.StringOrSymbol]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    attributes : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  void QV4::Object::insertMember(StringOrSymbol *s, const Value &v,
    #      PropertyAttributes attributes)
    self.uglySide.call(
        'ritual_ZN3QV46Object12insertMemberEPNS_14StringOrSymbolERKNS_5Valu'
        'eENS_18PropertyAttributesE',
        self._addressOf(s), self._valueOf(v), self._valueOf(attributes),
    )

  @overload(
      WAIT['QV4.StringOrSymbol'], WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      WAIT['QV4.StringOrSymbol'], NoneType, WAIT['QV4.PropertyAttributes'],
  )
  @overload(NoneType, WAIT['QV4.Property'], WAIT['QV4.PropertyAttributes'])
  @overload(NoneType, NoneType, WAIT['QV4.PropertyAttributes'])
  def insertMember(
      self,
      s: Optional[QV4.StringOrSymbol],
      p: Optional[QV4.Property],
      attributes: QV4.PropertyAttributes,
  ) -> None:
    """
    Calls Qt's 'void QV4::Object::insertMember(StringOrSymbol *s, const
    Property *p, PropertyAttributes attributes)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#insertMember

    Parameters
    ----------

    s : Optional[QV4.StringOrSymbol]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attributes : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  void QV4::Object::insertMember(StringOrSymbol *s, const Property *p,
    #      PropertyAttributes attributes)
    self.uglySide.call(
        'ritual_ZN3QV46Object12insertMemberEPNS_14StringOrSymbolEPKNS_8Prop'
        'ertyENS_18PropertyAttributesE',
        self._addressOf(s), self._addressOf(p), self._valueOf(attributes),
    )

  def preventExtensions(self) -> bool:
    """
    Calls Qt's 'bool QV4::Object::preventExtensions()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#preventExtensions
    """
    #  bool QV4::Object::preventExtensions()
    return self.uglySide.call('ritual_ZN3QV46Object17preventExtensionsEv')

  @overload(THIS)
  @overload(NoneType)
  def copyArrayData(self, other: Optional[Object]) -> None:
    """
    Calls Qt's 'void QV4::Object::copyArrayData(Object *other)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#copyArrayData

    Parameters
    ----------

    other : Optional[Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Object::copyArrayData(Object *other)
    self.uglySide.call(
        'ritual_ZN3QV46Object13copyArrayDataEPS0_', self._addressOf(other),
    )

  @overload(int, WAIT['QV4.Property'], WAIT['QV4.PropertyAttributes'])
  @overload(int, NoneType, WAIT['QV4.PropertyAttributes'])
  def arraySet(
      self,
      index: int,
      p: Optional[QV4.Property],
      attributes: QV4.PropertyAttributes,
  ) -> None:
    """
    Calls Qt's 'void QV4::Object::arraySet(uint index, const Property *p,
    PropertyAttributes attributes)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#arraySet

    Parameters
    ----------

    index : int
      Passed on as it is.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attributes : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  void QV4::Object::arraySet(uint index, const Property *p,
    #      PropertyAttributes attributes)
    self.uglySide.call(
        'ritual_ZN3QV46Object8arraySetEjPKNS_8PropertyENS_18PropertyAttribu'
        'tesE',
        index, self._addressOf(p), self._valueOf(attributes),
    )

  @overload(int, QV4.Value)
  def arraySet(self, index: int, value: QV4.Value) -> None:
    """
    Calls Qt's 'void QV4::Object::arraySet(uint index, const Value &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#arraySet

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::Object::arraySet(uint index, const Value &value)
    self.uglySide.call(
        'ritual_ZN3QV46Object8arraySetEjRKNS_5ValueE',
        index, self._valueOf(value),
    )

  @overload(int, QV4.Value)
  def arrayPut(self, index: int, value: QV4.Value) -> bool:
    """
    Calls Qt's 'bool QV4::Object::arrayPut(uint index, const Value &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#arrayPut

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  bool QV4::Object::arrayPut(uint index, const Value &value)
    return self.uglySide.call(
        'ritual_ZN3QV46Object8arrayPutEjRKNS_5ValueE',
        index, self._valueOf(value),
    )

  @overload(int, QV4.Value, int)
  @overload(int, NoneType, int)
  def arrayPut(
      self,
      index: int,
      values: Optional[QV4.Value],
      n: int,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::arrayPut(uint index, const Value *values,
    uint n)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#arrayPut

    Parameters
    ----------

    index : int
      Passed on as it is.

    values : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    n : int
      Passed on as it is.
    """
    #  bool QV4::Object::arrayPut(uint index, const Value *values, uint n)
    return self.uglySide.call(
        'ritual_ZN3QV46Object8arrayPutEjPKNS_5ValueEj',
        index, self._addressOf(values), n,
    )

  @overload(QV4.Value)
  def push_back(self, v: QV4.Value) -> None:
    """
    Calls Qt's 'void QV4::Object::push_back(const Value &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#push_back

    Parameters
    ----------

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::Object::push_back(const Value &v)
    self.uglySide.call(
        'ritual_ZN3QV46Object9push_backERKNS_5ValueE', self._valueOf(v),
    )

  @overload(int)
  def arrayReserve(self, n: int) -> None:
    """
    Calls Qt's 'void QV4::Object::arrayReserve(uint n)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#arrayReserve

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QV4::Object::arrayReserve(uint n)
    self.uglySide.call('ritual_ZN3QV46Object12arrayReserveEj', n)

  def arrayCreate(self) -> None:
    """
    Calls Qt's 'void QV4::Object::arrayCreate()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#arrayCreate
    """
    #  void QV4::Object::arrayCreate()
    self.uglySide.call('ritual_ZN3QV46Object11arrayCreateEv')

  def initSparseArray(self) -> None:
    """
    Calls Qt's 'void QV4::Object::initSparseArray()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#initSparseArray
    """
    #  void QV4::Object::initSparseArray()
    self.uglySide.call('ritual_ZN3QV46Object15initSparseArrayEv')

  def protoHasArray(self) -> bool:
    """
    Calls Qt's 'bool QV4::Object::protoHasArray()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#protoHasArray
    """
    #  bool QV4::Object::protoHasArray()
    return self.uglySide.call('ritual_ZN3QV46Object13protoHasArrayEv')

  @overload(WAIT['QV4.StringOrSymbol'], QV4.Value)
  @overload(NoneType, QV4.Value)
  @overload(WAIT['QV4.StringOrSymbol'], QV4.Value, QV4.Value)
  @overload(WAIT['QV4.StringOrSymbol'], QV4.Value, NoneType)
  @overload(NoneType, QV4.Value, QV4.Value)
  @overload(NoneType, QV4.Value, NoneType)
  def put(
      self,
      name: Optional[QV4.StringOrSymbol],
      v: QV4.Value,
      receiver: Optional[QV4.Value] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::put(StringOrSymbol *name, const Value &v,
    Value *receiver)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#put

    Parameters
    ----------

    name : Optional[QV4.StringOrSymbol]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    receiver : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QV4::Object::put(StringOrSymbol *name, const Value &v, Value
    #      *receiver)
    return self.uglySide.call(
        'ritual_ZN3QV46Object3putEPNS_14StringOrSymbolERKNS_5ValueEPS3_',
        self._addressOf(name), self._valueOf(v), self._addressOf(receiver),
    )

  @overload(int, QV4.Value)
  @overload(int, QV4.Value, QV4.Value)
  @overload(int, QV4.Value, NoneType)
  def put(
      self,
      idx: int,
      v: QV4.Value,
      receiver: Optional[QV4.Value] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::put(uint idx, const Value &v, Value
    *receiver)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#put

    Parameters
    ----------

    idx : int
      Passed on as it is.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    receiver : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QV4::Object::put(uint idx, const Value &v, Value *receiver)
    return self.uglySide.call(
        'ritual_ZN3QV46Object3putEjRKNS_5ValueEPS1_',
        idx, self._valueOf(v), self._addressOf(receiver),
    )

  @overload(WAIT['QV4.PropertyKey'], QV4.Value)
  @overload(WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  def put(
      self,
      id: QV4.PropertyKey,
      v: QV4.Value,
      receiver: Optional[QV4.Value] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::put(PropertyKey id, const Value &v, Value
    *receiver)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#put

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    receiver : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QV4::Object::put(PropertyKey id, const Value &v, Value *receiver)
    return self.uglySide.call(
        'ritual_ZN3QV46Object3putENS_11PropertyKeyERKNS_5ValueEPS2_',
        self._valueOf(id), self._valueOf(v), self._addressOf(receiver),
    )

  @overload(int, QV4.Value)
  def putIndexed(self, idx: int, v: QV4.Value) -> bool:
    """
    Calls Qt's 'bool QV4::Object::putIndexed(uint idx, const Value &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#putIndexed

    Parameters
    ----------

    idx : int
      Passed on as it is.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  bool QV4::Object::putIndexed(uint idx, const Value &v)
    return self.uglySide.call(
        'ritual_ZN3QV46Object10putIndexedEjRKNS_5ValueE',
        idx, self._valueOf(v),
    )

  @overload(WAIT['QV4.StringOrSymbol'], QV4.Value, ThrowOnFailure)
  @overload(NoneType, QV4.Value, ThrowOnFailure)
  def set(
      self,
      name: Optional[QV4.StringOrSymbol],
      v: QV4.Value,
      shouldThrow: ThrowOnFailure,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::set(StringOrSymbol *name, const Value &v,
    ThrowOnFailure shouldThrow)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#set

    Parameters
    ----------

    name : Optional[QV4.StringOrSymbol]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    shouldThrow : ThrowOnFailure
      Passed on as its number.
    """
    #  bool QV4::Object::set(StringOrSymbol *name, const Value &v,
    #      ThrowOnFailure shouldThrow)
    return self.uglySide.call(
        'ritual_ZN3QV46Object3setEPNS_14StringOrSymbolERKNS_5ValueENS0_14Th'
        'rowOnFailureE',
        self._addressOf(name), self._valueOf(v), shouldThrow.value,
    )

  @overload(WAIT['QV4.PropertyKey'])
  def deleteProperty(self, id: QV4.PropertyKey) -> bool:
    """
    Calls Qt's 'bool QV4::Object::deleteProperty(PropertyKey id)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#deleteProperty

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::Object::deleteProperty(PropertyKey id)
    return self.uglySide.call(
        'ritual_ZN3QV46Object14deletePropertyENS_11PropertyKeyE',
        self._valueOf(id),
    )

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Lookup'], QV4.Value)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, QV4.Value)
  @overload(NoneType, WAIT['QV4.Lookup'], QV4.Value)
  @overload(NoneType, NoneType, QV4.Value)
  def resolveLookupSetter(
      self,
      engine: Optional[QV4.ExecutionEngine],
      lookup: Optional[QV4.Lookup],
      value: QV4.Value,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::resolveLookupSetter(ExecutionEngine
    *engine, Lookup *lookup, const Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#resolveLookupSetter

    Parameters
    ----------

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
    #  bool QV4::Object::resolveLookupSetter(ExecutionEngine *engine, Lookup
    #      *lookup, const Value &value)
    return self.uglySide.call(
        'ritual_ZN3QV46Object19resolveLookupSetterEPNS_15ExecutionEngineEPN'
        'S_6LookupERKNS_5ValueE',
        self._addressOf(engine), self._addressOf(lookup),
        self._valueOf(value),
    )

  @overload(
      WAIT['QV4.ExecutionEngine'], int, WAIT['QV4.InternalClassEntry'],
      WAIT['QV4.Property'], WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], int, WAIT['QV4.InternalClassEntry'],
      NoneType, WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], int, NoneType, WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], int, NoneType, NoneType,
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      NoneType, int, WAIT['QV4.InternalClassEntry'], WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      NoneType, int, WAIT['QV4.InternalClassEntry'], NoneType,
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      NoneType, int, NoneType, WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      NoneType, int, NoneType, NoneType, WAIT['QV4.PropertyAttributes'],
  )
  def internalDefineOwnProperty(
      self,
      engine: Optional[QV4.ExecutionEngine],
      index: int,
      memberEntry: Optional[QV4.InternalClassEntry],
      p: Optional[QV4.Property],
      attrs: QV4.PropertyAttributes,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::internalDefineOwnProperty(ExecutionEngine
    *engine, uint index, const InternalClassEntry *memberEntry, const
    Property *p, PropertyAttributes attrs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#internalDefineOwnProperty

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    memberEntry : Optional[QV4.InternalClassEntry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  bool QV4::Object::internalDefineOwnProperty(ExecutionEngine *engine,
    #      uint index, const InternalClassEntry *memberEntry, const Property
    #      *p, PropertyAttributes attrs)
    return self.uglySide.call(
        'ritual_ZN3QV46Object25internalDefineOwnPropertyEPNS_15ExecutionEng'
        'ineEjPKNS_18InternalClassEntryEPKNS_8PropertyENS_18PropertyAttribu'
        'tesE',
        self._addressOf(engine), index, self._addressOf(memberEntry),
        self._addressOf(p), self._valueOf(attrs),
    )

  @overload(WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  def internalPut(
      self,
      id: QV4.PropertyKey,
      value: QV4.Value,
      receiver: Optional[QV4.Value],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Object::internalPut(PropertyKey id, const Value
    &value, Value *receiver)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-object.html#internalPut

    Parameters
    ----------

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
    #  bool QV4::Object::internalPut(PropertyKey id, const Value &value,
    #      Value *receiver)
    return self.uglySide.call(
        'ritual_ZN3QV46Object11internalPutENS_11PropertyKeyERKNS_5ValueEPS2'
        '_',
        self._valueOf(id), self._valueOf(value), self._addressOf(receiver),
    )

  @overload(WAIT['QV4.PropertyKey'])
  def internalDeleteProperty(self, id: QV4.PropertyKey) -> bool:
    """
    Calls Qt's 'bool QV4::Object::internalDeleteProperty(PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-object.html#internalDeleteProperty

    Parameters
    ----------

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::Object::internalDeleteProperty(PropertyKey id)
    return self.uglySide.call(
        'ritual_ZN3QV46Object22internalDeletePropertyENS_11PropertyKeyE',
        self._valueOf(id),
    )

  @staticmethod
  def arrayType(*__, **_) -> Never:
    """
    Qt's 'ArrayData::Type QV4::Object::arrayType() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.Object.arrayType' has no cute function yet. Qt's "
        "'ArrayData::Type QV4::Object::arrayType() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def defineAccessorProperty(*__, **_) -> Never:
    """
    - Qt's 'void QV4::Object::defineAccessorProperty(const QString &name,
      VTable::Call getter, VTable::Call setter)': takes a type Python has no
      way to hand over yet.
    - Qt's 'void QV4::Object::defineAccessorProperty(StringOrSymbol *name,
      VTable::Call getter, VTable::Call setter)': takes a type Python has no
      way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Object.defineAccessorProperty' has no cute function yet. Qt's "
        "'void QV4::Object::defineAccessorProperty(const QString &name, "
        "VTable::Call getter, VTable::Call setter)': takes a type Python "
        "has no way to hand over yet. Qt's 'void "
        "QV4::Object::defineAccessorProperty(StringOrSymbol *name, "
        "VTable::Call getter, VTable::Call setter)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def get(*__, **_) -> Never:
    """
    - Qt's 'ReturnedValue QV4::Object::get(StringOrSymbol *name, bool
      *hasProperty, const Value *receiver) const': takes a number to change
      where it is.
    - Qt's 'ReturnedValue QV4::Object::get(uint idx, bool *hasProperty, const
      Value *receiver) const': takes a number to change where it is.
    - Qt's 'ReturnedValue QV4::Object::get(PropertyKey id, const Value
      *receiver, bool *hasProperty) const': takes a number to change where it
      is.
    """
    raise NotImplementedError(
        "'QV4.Object.get' has no cute function yet. Qt's 'ReturnedValue "
        "QV4::Object::get(StringOrSymbol *name, bool *hasProperty, const "
        "Value *receiver) const': takes a number to change where it is. "
        "Qt's 'ReturnedValue QV4::Object::get(uint idx, bool *hasProperty, "
        "const Value *receiver) const': takes a number to change where it "
        "is. Qt's 'ReturnedValue QV4::Object::get(PropertyKey id, const "
        "Value *receiver, bool *hasProperty) const': takes a number to "
        "change where it is.")

  @staticmethod
  def getIndexed(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::Object::getIndexed(uint idx, bool *hasProperty)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QV4.Object.getIndexed' has no cute function yet. Qt's "
        "'ReturnedValue QV4::Object::getIndexed(uint idx, bool "
        "*hasProperty) const': takes a number to change where it is.")

  @staticmethod
  def internalGet(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::Object::internalGet(PropertyKey id, const Value
    *receiver, bool *hasProperty) const': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QV4.Object.internalGet' has no cute function yet. Qt's "
        "'ReturnedValue QV4::Object::internalGet(PropertyKey id, const "
        "Value *receiver, bool *hasProperty) const': takes a number to "
        "change where it is.")

  @staticmethod
  def metacall(*__, **_) -> Never:
    """
    Qt's 'int QV4::Object::metacall(QMetaObject::Call call, int index, void
    **a)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Object.metacall' has no cute function yet. Qt's 'int "
        "QV4::Object::metacall(QMetaObject::Call call, int index, void "
        "**a)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def ownPropertyKeys(*__, **_) -> Never:
    """
    Qt's 'OwnPropertyKeyIterator *QV4::Object::ownPropertyKeys(Value *target)
    const': gives 'QV4::OwnPropertyKeyIterator', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Object.ownPropertyKeys' has no cute function yet. Qt's "
        "'OwnPropertyKeyIterator *QV4::Object::ownPropertyKeys(Value "
        "*target) const': gives 'QV4::OwnPropertyKeyIterator', which has no "
        "cute class yet.")

  @staticmethod
  def speciesConstructor(*__, **_) -> Never:
    """
    Qt's 'const FunctionObject *QV4::Object::speciesConstructor(Scope &scope,
    const FunctionObject *defaultConstructor) const': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Object.speciesConstructor' has no cute function yet. Qt's "
        "'const FunctionObject *QV4::Object::speciesConstructor(Scope "
        "&scope, const FunctionObject *defaultConstructor) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def virtualGet(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::Object::virtualGet(const Managed *m, PropertyKey
    id, const Value *receiver, bool *hasProperty)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QV4.Object.virtualGet' has no cute function yet. Qt's "
        "'ReturnedValue QV4::Object::virtualGet(const Managed *m, "
        "PropertyKey id, const Value *receiver, bool *hasProperty)': takes "
        "a number to change where it is.")

  @staticmethod
  def virtualMetacall(*__, **_) -> Never:
    """
    Qt's 'int QV4::Object::virtualMetacall(Object *object, QMetaObject::Call
    call, int index, void **a)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QV4.Object.virtualMetacall' has no cute function yet. Qt's 'int "
        "QV4::Object::virtualMetacall(Object *object, QMetaObject::Call "
        "call, int index, void **a)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def virtualOwnPropertyKeys(*__, **_) -> Never:
    """
    Qt's 'OwnPropertyKeyIterator *QV4::Object::virtualOwnPropertyKeys(const
    Object *m, Value *target)': gives 'QV4::OwnPropertyKeyIterator', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Object.virtualOwnPropertyKeys' has no cute function yet. Qt's "
        "'OwnPropertyKeyIterator *QV4::Object::virtualOwnPropertyKeys(const "
        "Object *m, Value *target)': gives 'QV4::OwnPropertyKeyIterator', "
        "which has no cute class yet.")
