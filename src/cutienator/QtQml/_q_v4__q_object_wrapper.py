"""
QV4::QObjectWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::QObjectWrapper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QMetaObject
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QQmlPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlPropertyData = WAIT['QQmlPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QObjectWrapper(QV4.Object):
  """
  The cute side of Qt's QV4::QObjectWrapper: a plain Python object standing
  in front of one C++ QV4::QObjectWrapper.

  It is built on the cute 'QV4::Object', as Qt's QV4::QObjectWrapper is built
  on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::QObjectWrapper that has a ritual and that
  Python can call so far, 25 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualDestroy', 'initializeBindings', 'metaObject', 'object', 'wrap',
  'wrapConst', 'ensureWrapper', 'markWrapper', 'setProperty',
  'destroyObject', 'getProperty', 'virtualResolveLookupGetter',
  'virtualResolveLookupSetter', 'objectToString', 'virtualIsEqualTo',
  'create', 'virtualPut', 'virtualGetOwnProperty', 'method_connect',
  'method_disconnect', 'wrap_slowPath', 'wrapConst_slowPath'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::QObjectWrapper::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'ReturnedValue QV4::QObjectWrapper::getQmlProperty(const
    QQmlRefPointer<QQmlContextData> &qmlContext, String *name, Flags flags,
    bool *hasProperty) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'ReturnedValue QV4::QObjectWrapper::getQmlProperty(ExecutionEngine
    *engine, const QQmlRefPointer<QQmlContextData> &qmlContext, Heap::Object
    *wrapper, QObject *object, String *name, Flags flags, bool *hasProperty,
    const QQmlPropertyData **property)': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QV4::QObjectWrapper::setQmlProperty(ExecutionEngine *engine,
    const QQmlRefPointer<QQmlContextData> &qmlContext, QObject *object,
    String *name, Flags flags, const Value &value)': takes a type Python has
    no way to hand over yet.
  - Qt's 'OwnPropertyKeyIterator
    *QV4::QObjectWrapper::virtualOwnPropertyKeys(const Object *m, Value
    *target)': gives 'QV4::OwnPropertyKeyIterator', which has no cute class
    yet.
  - Qt's 'int QV4::QObjectWrapper::virtualMetacall(Object *object,
    QMetaObject::Call call, int index, void **a)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QQmlPropertyData *QV4::QObjectWrapper::findProperty(QObject
    *o, const QQmlRefPointer<QQmlContextData> &qmlContext, String *name,
    Flags flags, QQmlPropertyData *local)': takes a type Python has no way to
    hand over yet.
  - Qt's 'const QQmlPropertyData *QV4::QObjectWrapper::findProperty(const
    QQmlRefPointer<QQmlContextData> &qmlContext, String *name, Flags flags,
    QQmlPropertyData *local) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'ReturnedValue QV4::QObjectWrapper::virtualGet(const Managed *m,
    PropertyKey id, const Value *receiver, bool *hasProperty)': takes a
    number to change where it is.

  What has no ritual
  ------------------

  6 of the 42 functions Qt declares: 3 forbidden; 2 a template; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::QObjectWrapper is created at the first use, not by
    'QV4::QObjectWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::QObjectWrapper.
  - Each name of Qt's QV4::QObjectWrapper that has no cute function yet,
    'findProperty', 'getQmlProperty', 'lookupMethodGetterImpl',
    'lookupPropertyGetterImpl', 'setQmlProperty', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::QObjectWrapper, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QV4::QObjectWrapper::Flag' of Qt, with the 5 names Qt
    gives in it. Qt names the type of its combinations
    'QV4::QObjectWrapper::Flags'.
    """

    NoFlag = 0x0
    CheckRevision = 0x1
    AttachMethods = 0x2
    AllowOverride = 0x4
    IncludeImports = 0x8

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::QObjectWrapper::virtualDestroy(QV4::Heap::Base
    *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QObjectWrapper::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV414QObjectWrapper14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def initializeBindings(engine: Optional[QV4.ExecutionEngine]) -> None:
    """
    Calls Qt's 'void QV4::QObjectWrapper::initializeBindings(ExecutionEngine
    *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#initializeBindings

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QObjectWrapper::initializeBindings(ExecutionEngine *engine)
    Rituals.call(
        'ritual_ZN3QV414QObjectWrapper18initializeBindingsEPNS_15ExecutionE'
        'ngineE',
        CuteMixin._addressOf(engine),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QObject)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def wrap(
      engine: Optional[QV4.ExecutionEngine],
      object: Optional[QObject],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QObjectWrapper::wrap(ExecutionEngine
    *engine, QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#wrap

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QObjectWrapper::wrap(ExecutionEngine *engine,
    #      QObject *object)
    return Rituals.call(
        'ritual_ZN3QV414QObjectWrapper4wrapEPNS_15ExecutionEngineEP7QObject',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(object,
        'QObject'),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QObject)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def wrapConst(
      engine: Optional[QV4.ExecutionEngine],
      object: Optional[QObject],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QObjectWrapper::wrapConst(ExecutionEngine
    *engine, QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#wrapConst

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QObjectWrapper::wrapConst(ExecutionEngine *engine,
    #      QObject *object)
    return Rituals.call(
        'ritual_ZN3QV414QObjectWrapper9wrapConstEPNS_15ExecutionEngineEP7QO'
        'bject',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(object,
        'QObject'),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QObject)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def ensureWrapper(
      engine: Optional[QV4.ExecutionEngine],
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QV4::QObjectWrapper::ensureWrapper(ExecutionEngine
    *engine, QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#ensureWrapper

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QObjectWrapper::ensureWrapper(ExecutionEngine *engine,
    #      QObject *object)
    Rituals.call(
        'ritual_ZN3QV414QObjectWrapper13ensureWrapperEPNS_15ExecutionEngine'
        'EP7QObject',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(object,
        'QObject'),
    )

  @staticmethod
  @overload(QObject, WAIT['QV4.MarkStack'])
  @overload(QObject, NoneType)
  @overload(NoneType, WAIT['QV4.MarkStack'])
  @overload(NoneType, NoneType)
  def markWrapper(
      object: Optional[QObject],
      markStack: Optional[QV4.MarkStack],
  ) -> None:
    """
    Calls Qt's 'void QV4::QObjectWrapper::markWrapper(QObject *object,
    MarkStack *markStack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#markWrapper

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QObjectWrapper::markWrapper(QObject *object, MarkStack
    #      *markStack)
    Rituals.call(
        'ritual_ZN3QV414QObjectWrapper11markWrapperEP7QObjectPNS_9MarkStack'
        'E',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._addressOf(markStack),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QObject, int, QV4.Value)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, int, QV4.Value)
  @overload(NoneType, QObject, int, QV4.Value)
  @overload(NoneType, NoneType, int, QV4.Value)
  def setProperty(
      engine: Optional[QV4.ExecutionEngine],
      object: Optional[QObject],
      propertyIndex: int,
      value: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QV4::QObjectWrapper::setProperty(ExecutionEngine
    *engine, QObject *object, int propertyIndex, const Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#setProperty

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyIndex : int
      Passed on as it is.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::QObjectWrapper::setProperty(ExecutionEngine *engine, QObject
    #      *object, int propertyIndex, const Value &value)
    Rituals.call(
        'ritual_ZN3QV414QObjectWrapper11setPropertyEPNS_15ExecutionEngineEP'
        '7QObjectiRKNS_5ValueE',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(object,
        'QObject'), propertyIndex, CuteMixin._valueOf(value),
    )

  @overload(WAIT['QV4.ExecutionEngine'], int, QV4.Value)
  @overload(NoneType, int, QV4.Value)
  def setProperty(
      self,
      engine: Optional[QV4.ExecutionEngine],
      propertyIndex: int,
      value: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QV4::QObjectWrapper::setProperty(ExecutionEngine
    *engine, int propertyIndex, const Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#setProperty

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyIndex : int
      Passed on as it is.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::QObjectWrapper::setProperty(ExecutionEngine *engine, int
    #      propertyIndex, const Value &value)
    self.uglySide.call(
        'ritual_ZN3QV414QObjectWrapper11setPropertyEPNS_15ExecutionEngineEi'
        'RKNS_5ValueE',
        self._addressOf(engine), propertyIndex, self._valueOf(value),
    )

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], QObject, QQmlPropertyData, QV4.Value,
  )
  @overload(WAIT['QV4.ExecutionEngine'], QObject, NoneType, QV4.Value)
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, QQmlPropertyData, QV4.Value,
  )
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, NoneType, QV4.Value)
  @overload(NoneType, QObject, QQmlPropertyData, QV4.Value)
  @overload(NoneType, QObject, NoneType, QV4.Value)
  @overload(NoneType, NoneType, QQmlPropertyData, QV4.Value)
  @overload(NoneType, NoneType, NoneType, QV4.Value)
  def setProperty(
      engine: Optional[QV4.ExecutionEngine],
      object: Optional[QObject],
      property: Optional[QQmlPropertyData],
      value: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QV4::QObjectWrapper::setProperty(ExecutionEngine
    *engine, QObject *object, const QQmlPropertyData *property, const Value
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#setProperty

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::QObjectWrapper::setProperty(ExecutionEngine *engine, QObject
    #      *object, const QQmlPropertyData *property, const Value &value)
    Rituals.call(
        'ritual_ZN3QV414QObjectWrapper11setPropertyEPNS_15ExecutionEngineEP'
        '7QObjectPK16QQmlPropertyDataRKNS_5ValueE',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(object,
        'QObject'), CuteMixin._addressOf(property),
        CuteMixin._valueOf(value),
    )

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.Object'], QObject,
      QQmlPropertyData, Flags,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.Object'], QObject,
      NoneType, Flags,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.Object'], NoneType,
      QQmlPropertyData, Flags,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.Object'], NoneType,
      NoneType, Flags,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, QObject, QQmlPropertyData,
      Flags,
  )
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, QObject, NoneType, Flags)
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, NoneType, QQmlPropertyData,
      Flags,
  )
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, NoneType, NoneType, Flags)
  @overload(
      NoneType, WAIT['QV4.Heap.Object'], QObject, QQmlPropertyData, Flags,
  )
  @overload(NoneType, WAIT['QV4.Heap.Object'], QObject, NoneType, Flags)
  @overload(
      NoneType, WAIT['QV4.Heap.Object'], NoneType, QQmlPropertyData, Flags,
  )
  @overload(NoneType, WAIT['QV4.Heap.Object'], NoneType, NoneType, Flags)
  @overload(NoneType, NoneType, QObject, QQmlPropertyData, Flags)
  @overload(NoneType, NoneType, QObject, NoneType, Flags)
  @overload(NoneType, NoneType, NoneType, QQmlPropertyData, Flags)
  @overload(NoneType, NoneType, NoneType, NoneType, Flags)
  def getProperty(
      engine: Optional[QV4.ExecutionEngine],
      wrapper: Optional[QV4.Heap.Object],
      object: Optional[QObject],
      property: Optional[QQmlPropertyData],
      flags: Flags,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QObjectWrapper::getProperty(ExecutionEngine *engine, Heap::Object
    *wrapper, QObject *object, const QQmlPropertyData *property, Flags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#getProperty

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    wrapper : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : Flags
      Passed on as its number.
    """
    #  ReturnedValue QV4::QObjectWrapper::getProperty(ExecutionEngine
    #      *engine, Heap::Object *wrapper, QObject *object, const
    #      QQmlPropertyData *property, Flags flags)
    return Rituals.call(
        'ritual_ZN3QV414QObjectWrapper11getPropertyEPNS_15ExecutionEngineEP'
        'NS_4Heap6ObjectEP7QObjectPK16QQmlPropertyData6QFlagsINS0_4FlagEE',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(wrapper),
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._addressOf(property), flags.value,
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
    QV4::QObjectWrapper::virtualResolveLookupGetter(const Object *object,
    ExecutionEngine *engine, Lookup *lookup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#virtualResolveLookupGetter

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
    #  ReturnedValue QV4::QObjectWrapper::virtualResolveLookupGetter(const
    #      Object *object, ExecutionEngine *engine, Lookup *lookup)
    return Rituals.call(
        'ritual_ZN3QV414QObjectWrapper26virtualResolveLookupGetterEPKNS_6Ob'
        'jectEPNS_15ExecutionEngineEPNS_6LookupE',
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
    Calls Qt's 'bool QV4::QObjectWrapper::virtualResolveLookupSetter(Object
    *object, ExecutionEngine *engine, Lookup *lookup, const Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#virtualResolveLookupSetter

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
    #  bool QV4::QObjectWrapper::virtualResolveLookupSetter(Object *object,
    #      ExecutionEngine *engine, Lookup *lookup, const Value &value)
    return Rituals.call(
        'ritual_ZN3QV414QObjectWrapper26virtualResolveLookupSetterEPNS_6Obj'
        'ectEPNS_15ExecutionEngineEPNS_6LookupERKNS_5ValueE',
        CuteMixin._addressOf(object), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(lookup), CuteMixin._valueOf(value),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QMetaObject, QObject)
  @overload(WAIT['QV4.ExecutionEngine'], QMetaObject, NoneType)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, QObject)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, NoneType)
  @overload(NoneType, QMetaObject, QObject)
  @overload(NoneType, QMetaObject, NoneType)
  @overload(NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType)
  def objectToString(
      engine: Optional[QV4.ExecutionEngine],
      metaObject: Optional[QMetaObject],
      object: Optional[QObject],
  ) -> str:
    """
    Calls Qt's 'QString QV4::QObjectWrapper::objectToString(ExecutionEngine
    *engine, const QMetaObject *metaObject, QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#objectToString

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::QObjectWrapper::objectToString(ExecutionEngine *engine,
    #      const QMetaObject *metaObject, QObject *object)
    return Rituals.call(
        'ritual_ZN3QV414QObjectWrapper14objectToStringEPNS_15ExecutionEngin'
        'eEPK11QMetaObjectP7QObject',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(metaObject,
        'QMetaObject'), CuteMixin._addressOf(object, 'QObject'),
    )

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
    Calls Qt's 'bool QV4::QObjectWrapper::virtualIsEqualTo(Managed *that,
    Managed *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#virtualIsEqualTo

    Parameters
    ----------

    that : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    o : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::QObjectWrapper::virtualIsEqualTo(Managed *that, Managed *o)
    return Rituals.call(
        'ritual_ZN3QV414QObjectWrapper16virtualIsEqualToEPNS_7ManagedES2_',
        CuteMixin._addressOf(that), CuteMixin._addressOf(o),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QObject)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def create(
      engine: Optional[QV4.ExecutionEngine],
      object: Optional[QObject],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QObjectWrapper::create(ExecutionEngine
    *engine, QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#create

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QObjectWrapper::create(ExecutionEngine *engine,
    #      QObject *object)
    return Rituals.call(
        'ritual_ZN3QV414QObjectWrapper6createEPNS_15ExecutionEngineEP7QObje'
        'ct',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(object,
        'QObject'),
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
    Calls Qt's 'bool QV4::QObjectWrapper::virtualPut(Managed *m, PropertyKey
    id, const Value &value, Value *receiver)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#virtualPut

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
    #  bool QV4::QObjectWrapper::virtualPut(Managed *m, PropertyKey id, const
    #      Value &value, Value *receiver)
    return Rituals.call(
        'ritual_ZN3QV414QObjectWrapper10virtualPutEPNS_7ManagedENS_11Proper'
        'tyKeyERKNS_5ValueEPS4_',
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
    QV4::QObjectWrapper::virtualGetOwnProperty(const Managed *m, PropertyKey
    id, Property *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#virtualGetOwnProperty

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
    #  PropertyAttributes QV4::QObjectWrapper::virtualGetOwnProperty(const
    #      Managed *m, PropertyKey id, Property *p)
    address = Rituals.call(
        'ritual_ZN3QV414QObjectWrapper21virtualGetOwnPropertyEPKNS_7Managed'
        'ENS_11PropertyKeyEPNS_8PropertyE',
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
  def method_connect(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QObjectWrapper::method_connect(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#method_connect

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
    #  ReturnedValue QV4::QObjectWrapper::method_connect(const FunctionObject
    #      *a0, const Value *thisObject, const Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN3QV414QObjectWrapper14method_connectEPKNS_14FunctionObjec'
        'tEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], QV4.Value, NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, QV4.Value, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, QV4.Value, QV4.Value, int)
  @overload(NoneType, QV4.Value, NoneType, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_disconnect(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QObjectWrapper::method_disconnect(const
    FunctionObject *a0, const Value *thisObject, const Value *argv, int
    argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#method_disconnect

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
    #  ReturnedValue QV4::QObjectWrapper::method_disconnect(const
    #      FunctionObject *a0, const Value *thisObject, const Value *argv,
    #      int argc)
    return Rituals.call(
        'ritual_ZN3QV414QObjectWrapper17method_disconnectEPKNS_14FunctionOb'
        'jectEPKNS_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QObject)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def wrap_slowPath(
      engine: Optional[QV4.ExecutionEngine],
      object: Optional[QObject],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QObjectWrapper::wrap_slowPath(ExecutionEngine *engine, QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#wrap_slowPath

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QObjectWrapper::wrap_slowPath(ExecutionEngine
    #      *engine, QObject *object)
    return Rituals.call(
        'ritual_ZN3QV414QObjectWrapper13wrap_slowPathEPNS_15ExecutionEngine'
        'EP7QObject',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(object,
        'QObject'),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QObject)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def wrapConst_slowPath(
      engine: Optional[QV4.ExecutionEngine],
      object: Optional[QObject],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QObjectWrapper::wrapConst_slowPath(ExecutionEngine *engine, QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#wrapConst_slowPath

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QObjectWrapper::wrapConst_slowPath(ExecutionEngine
    #      *engine, QObject *object)
    return Rituals.call(
        'ritual_ZN3QV414QObjectWrapper18wrapConst_slowPathEPNS_15ExecutionE'
        'ngineEP7QObject',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(object,
        'QObject'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::QObjectWrapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.QObjectWrapper]:
    """
    Calls Qt's 'QV4::Heap::QObjectWrapper *QV4::QObjectWrapper::d_unchecked()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.QObjectWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QObjectWrapper *QV4::QObjectWrapper::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV414QObjectWrapper11d_uncheckedEv',
    )
    return QV4.Heap.QObjectWrapper._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.QObjectWrapper]:
    """
    Calls Qt's 'QV4::Heap::QObjectWrapper *QV4::QObjectWrapper::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#d

    Returns
    -------

    Optional[QV4.Heap.QObjectWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QObjectWrapper *QV4::QObjectWrapper::d() const
    address = self.uglySide.call('ritual_ZNK3QV414QObjectWrapper1dEv')
    return QV4.Heap.QObjectWrapper._cuteAt(address)

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QV4::QObjectWrapper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QV4::QObjectWrapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV414QObjectWrapper10metaObjectEv',
    )
    return QMetaObject._cuteAt(address)

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QV4::QObjectWrapper::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QV4::QObjectWrapper::object() const
    address = self.uglySide.call('ritual_ZNK3QV414QObjectWrapper6objectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

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
    Calls Qt's 'void QV4::QObjectWrapper::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#__dataTest
    """
    #  void QV4::QObjectWrapper::__dataTest()
    self.uglySide.call('ritual_ZN3QV414QObjectWrapper10__dataTestEv')

  @overload(bool)
  def destroyObject(self, lastCall: bool) -> None:
    """
    Calls Qt's 'void QV4::QObjectWrapper::destroyObject(bool lastCall)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qobjectwrapper.html#destroyObject

    Parameters
    ----------

    lastCall : bool
      Passed on as it is.
    """
    #  void QV4::QObjectWrapper::destroyObject(bool lastCall)
    self.uglySide.call(
        'ritual_ZN3QV414QObjectWrapper13destroyObjectEb', lastCall,
    )

  @staticmethod
  def findProperty(*__, **_) -> Never:
    """
    - Qt's 'const QQmlPropertyData *QV4::QObjectWrapper::findProperty(QObject
      *o, const QQmlRefPointer<QQmlContextData> &qmlContext, String *name,
      Flags flags, QQmlPropertyData *local)': takes a type Python has no way
      to hand over yet.
    - Qt's 'const QQmlPropertyData *QV4::QObjectWrapper::findProperty(const
      QQmlRefPointer<QQmlContextData> &qmlContext, String *name, Flags flags,
      QQmlPropertyData *local) const': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QV4.QObjectWrapper.findProperty' has no cute function yet. Qt's "
        "'const QQmlPropertyData *QV4::QObjectWrapper::findProperty(QObject "
        "*o, const QQmlRefPointer<QQmlContextData> &qmlContext, String "
        "*name, Flags flags, QQmlPropertyData *local)': takes a type Python "
        "has no way to hand over yet. Qt's 'const QQmlPropertyData "
        "*QV4::QObjectWrapper::findProperty(const "
        "QQmlRefPointer<QQmlContextData> &qmlContext, String *name, Flags "
        "flags, QQmlPropertyData *local) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def getQmlProperty(*__, **_) -> Never:
    """
    - Qt's 'ReturnedValue QV4::QObjectWrapper::getQmlProperty(const
      QQmlRefPointer<QQmlContextData> &qmlContext, String *name, Flags flags,
      bool *hasProperty) const': takes a type Python has no way to hand over
      yet.
    - Qt's 'ReturnedValue QV4::QObjectWrapper::getQmlProperty(ExecutionEngine
      *engine, const QQmlRefPointer<QQmlContextData> &qmlContext,
      Heap::Object *wrapper, QObject *object, String *name, Flags flags, bool
      *hasProperty, const QQmlPropertyData **property)': takes a type Python
      has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.QObjectWrapper.getQmlProperty' has no cute function yet. Qt's "
        "'ReturnedValue QV4::QObjectWrapper::getQmlProperty(const "
        "QQmlRefPointer<QQmlContextData> &qmlContext, String *name, Flags "
        "flags, bool *hasProperty) const': takes a type Python has no way "
        "to hand over yet. Qt's 'ReturnedValue "
        "QV4::QObjectWrapper::getQmlProperty(ExecutionEngine *engine, const "
        "QQmlRefPointer<QQmlContextData> &qmlContext, Heap::Object "
        "*wrapper, QObject *object, String *name, Flags flags, bool "
        "*hasProperty, const QQmlPropertyData **property)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def lookupMethodGetterImpl(*__, **_) -> Never:
    """
    Qt's 'QV4::QObjectWrapper::lookupMethodGetterImpl': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QV4.QObjectWrapper.lookupMethodGetterImpl' has no cute function "
        "yet. Qt's 'QV4::QObjectWrapper::lookupMethodGetterImpl': a "
        "template: a pattern and no single function.")

  @staticmethod
  def lookupPropertyGetterImpl(*__, **_) -> Never:
    """
    Qt's 'QV4::QObjectWrapper::lookupPropertyGetterImpl': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QV4.QObjectWrapper.lookupPropertyGetterImpl' has no cute function "
        "yet. Qt's 'QV4::QObjectWrapper::lookupPropertyGetterImpl': a "
        "template: a pattern and no single function.")

  @staticmethod
  def setQmlProperty(*__, **_) -> Never:
    """
    Qt's 'bool QV4::QObjectWrapper::setQmlProperty(ExecutionEngine *engine,
    const QQmlRefPointer<QQmlContextData> &qmlContext, QObject *object,
    String *name, Flags flags, const Value &value)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.QObjectWrapper.setQmlProperty' has no cute function yet. Qt's "
        "'bool QV4::QObjectWrapper::setQmlProperty(ExecutionEngine *engine, "
        "const QQmlRefPointer<QQmlContextData> &qmlContext, QObject "
        "*object, String *name, Flags flags, const Value &value)': takes a "
        "type Python has no way to hand over yet.")
