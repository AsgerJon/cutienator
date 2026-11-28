"""
QV4::QQmlContextWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::QQmlContextWrapper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlContextWrapper(QV4.Object):
  """
  The cute side of Qt's QV4::QQmlContextWrapper: a plain Python object
  standing in front of one C++ QV4::QQmlContextWrapper.

  It is built on the cute 'QV4::Object', as Qt's QV4::QQmlContextWrapper is
  built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::QQmlContextWrapper that has a ritual and that
  Python can call so far, 21 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualDestroy', 'defaultInternalClass', 'getScopeObject', 'virtualPut',
  'resolveQmlContextPropertyLookupGetter', 'lookupScript', 'lookupSingleton',
  'lookupValueSingleton', 'lookupIdObject', 'lookupIdObjectInParentContext',
  'lookupScopeObjectProperty', 'lookupScopeObjectMethod',
  'lookupScopeFallbackProperty', 'lookupContextObjectProperty',
  'lookupContextObjectMethod', 'lookupInGlobalObject',
  'lookupInParentContextHierarchy', 'lookupType'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::QQmlContextWrapper::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'QQmlRefPointer<QQmlContextData>
    QV4::QQmlContextWrapper::getContext() const': gives a type Python has no
    way to take yet.
  - Qt's 'ReturnedValue QV4::QQmlContextWrapper::getPropertyAndBase(const
    QQmlContextWrapper *resource, PropertyKey id, const Value *receiver, bool
    *hasProperty, Value *base, Lookup *lookup)': takes a number to change
    where it is.
  - Qt's 'ReturnedValue QV4::QQmlContextWrapper::virtualGet(const Managed *m,
    PropertyKey id, const Value *receiver, bool *hasProperty)': takes a
    number to change where it is.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::QQmlContextWrapper is created at the first use, not by
    'QV4::QQmlContextWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::QQmlContextWrapper.
  - Each name of Qt's QV4::QQmlContextWrapper that has no cute function yet,
    'getContext', 'getPropertyAndBase', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::QQmlContextWrapper::virtualDestroy(QV4::Heap::Base
    *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QQmlContextWrapper::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def defaultInternalClass(
      e: Optional[QV4.EngineBase],
  ) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass
    *QV4::QQmlContextWrapper::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html#defaultInternalClass

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
    #  Heap::InternalClass
    #      *QV4::QQmlContextWrapper::defaultInternalClass(QV4::EngineBase *e)
    address = Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper20defaultInternalClassEPNS_10Engi'
        'neBaseE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

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
    Calls Qt's 'bool QV4::QQmlContextWrapper::virtualPut(Managed *m,
    PropertyKey id, const Value &value, Value *receiver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html#virtualPut

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
    #  bool QV4::QQmlContextWrapper::virtualPut(Managed *m, PropertyKey id,
    #      const Value &value, Value *receiver)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper10virtualPutEPNS_7ManagedENS_11Pr'
        'opertyKeyERKNS_5ValueEPS4_',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._valueOf(value), CuteMixin._addressOf(receiver),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def resolveQmlContextPropertyLookupGetter(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlContextWrapper::resolveQmlContextPropertyLookupGetter(Lookup *l,
    ExecutionEngine *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue
    #      QV4::QQmlContextWrapper::resolveQmlContextPropertyLookupGetter(
    #      Lookup *l, ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper37resolveQmlContextPropertyLookup'
        'GetterEPNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def lookupScript(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QQmlContextWrapper::lookupScript(Lookup
    *l, ExecutionEngine *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html#lookupScript

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QQmlContextWrapper::lookupScript(Lookup *l,
    #      ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper12lookupScriptEPNS_6LookupEPNS_15'
        'ExecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def lookupSingleton(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QQmlContextWrapper::lookupSingleton(Lookup
    *l, ExecutionEngine *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html#lookupSingleton

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QQmlContextWrapper::lookupSingleton(Lookup *l,
    #      ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper15lookupSingletonEPNS_6LookupEPNS'
        '_15ExecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def lookupValueSingleton(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlContextWrapper::lookupValueSingleton(Lookup *l, ExecutionEngine
    *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html#lookupValueSingleton

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QQmlContextWrapper::lookupValueSingleton(Lookup *l,
    #      ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper20lookupValueSingletonEPNS_6Looku'
        'pEPNS_15ExecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def lookupIdObject(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QQmlContextWrapper::lookupIdObject(Lookup
    *l, ExecutionEngine *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html#lookupIdObject

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QQmlContextWrapper::lookupIdObject(Lookup *l,
    #      ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper14lookupIdObjectEPNS_6LookupEPNS_'
        '15ExecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def lookupIdObjectInParentContext(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlContextWrapper::lookupIdObjectInParentContext(Lookup *l,
    ExecutionEngine *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue
    #      QV4::QQmlContextWrapper::lookupIdObjectInParentContext(Lookup *l,
    #      ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper29lookupIdObjectInParentContextEP'
        'NS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def lookupScopeObjectProperty(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlContextWrapper::lookupScopeObjectProperty(Lookup *l,
    ExecutionEngine *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue
    #      QV4::QQmlContextWrapper::lookupScopeObjectProperty(Lookup *l,
    #      ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper25lookupScopeObjectPropertyEPNS_6'
        'LookupEPNS_15ExecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def lookupScopeObjectMethod(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlContextWrapper::lookupScopeObjectMethod(Lookup *l,
    ExecutionEngine *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QQmlContextWrapper::lookupScopeObjectMethod(Lookup
    #      *l, ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper23lookupScopeObjectMethodEPNS_6Lo'
        'okupEPNS_15ExecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def lookupScopeFallbackProperty(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlContextWrapper::lookupScopeFallbackProperty(Lookup *l,
    ExecutionEngine *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue
    #      QV4::QQmlContextWrapper::lookupScopeFallbackProperty(Lookup *l,
    #      ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper27lookupScopeFallbackPropertyEPNS'
        '_6LookupEPNS_15ExecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def lookupContextObjectProperty(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlContextWrapper::lookupContextObjectProperty(Lookup *l,
    ExecutionEngine *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue
    #      QV4::QQmlContextWrapper::lookupContextObjectProperty(Lookup *l,
    #      ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper27lookupContextObjectPropertyEPNS'
        '_6LookupEPNS_15ExecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def lookupContextObjectMethod(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlContextWrapper::lookupContextObjectMethod(Lookup *l,
    ExecutionEngine *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue
    #      QV4::QQmlContextWrapper::lookupContextObjectMethod(Lookup *l,
    #      ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper25lookupContextObjectMethodEPNS_6'
        'LookupEPNS_15ExecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def lookupInGlobalObject(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlContextWrapper::lookupInGlobalObject(Lookup *l, ExecutionEngine
    *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html#lookupInGlobalObject

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QQmlContextWrapper::lookupInGlobalObject(Lookup *l,
    #      ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper20lookupInGlobalObjectEPNS_6Looku'
        'pEPNS_15ExecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def lookupInParentContextHierarchy(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QQmlContextWrapper::lookupInParentContextHierarchy(Lookup *l,
    ExecutionEngine *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue
    #      QV4::QQmlContextWrapper::lookupInParentContextHierarchy(Lookup *l,
    #      ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper30lookupInParentContextHierarchyE'
        'PNS_6LookupEPNS_15ExecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  @staticmethod
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(WAIT['QV4.Lookup'], WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(WAIT['QV4.Lookup'], NoneType, QV4.Value)
  @overload(WAIT['QV4.Lookup'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], QV4.Value)
  @overload(NoneType, WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, NoneType, QV4.Value)
  @overload(NoneType, NoneType, NoneType)
  def lookupType(
      l: Optional[QV4.Lookup],
      engine: Optional[QV4.ExecutionEngine],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QQmlContextWrapper::lookupType(Lookup *l,
    ExecutionEngine *engine, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html#lookupType

    Parameters
    ----------

    l : Optional[QV4.Lookup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::QQmlContextWrapper::lookupType(Lookup *l,
    #      ExecutionEngine *engine, Value *base)
    return Rituals.call(
        'ritual_ZN3QV418QQmlContextWrapper10lookupTypeEPNS_6LookupEPNS_15Ex'
        'ecutionEngineEPNS_5ValueE',
        CuteMixin._addressOf(l), CuteMixin._addressOf(engine),
        CuteMixin._addressOf(base),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::QQmlContextWrapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.QQmlContextWrapper]:
    """
    Calls Qt's 'QV4::Heap::QQmlContextWrapper
    *QV4::QQmlContextWrapper::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.QQmlContextWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QQmlContextWrapper *QV4::QQmlContextWrapper::d_unchecked()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV418QQmlContextWrapper11d_uncheckedEv',
    )
    return QV4.Heap.QQmlContextWrapper._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.QQmlContextWrapper]:
    """
    Calls Qt's 'QV4::Heap::QQmlContextWrapper *QV4::QQmlContextWrapper::d()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html#d

    Returns
    -------

    Optional[QV4.Heap.QQmlContextWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QQmlContextWrapper *QV4::QQmlContextWrapper::d() const
    address = self.uglySide.call('ritual_ZNK3QV418QQmlContextWrapper1dEv')
    return QV4.Heap.QQmlContextWrapper._cuteAt(address)

  def getScopeObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QV4::QQmlContextWrapper::getScopeObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html#getScopeObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QV4::QQmlContextWrapper::getScopeObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV418QQmlContextWrapper14getScopeObjectEv',
    )
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
    Calls Qt's 'void QV4::QQmlContextWrapper::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qqmlcontextwrapper.html#__dataTest
    """
    #  void QV4::QQmlContextWrapper::__dataTest()
    self.uglySide.call('ritual_ZN3QV418QQmlContextWrapper10__dataTestEv')

  @staticmethod
  def getContext(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData>
    QV4::QQmlContextWrapper::getContext() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QV4.QQmlContextWrapper.getContext' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> "
        "QV4::QQmlContextWrapper::getContext() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def getPropertyAndBase(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::QQmlContextWrapper::getPropertyAndBase(const
    QQmlContextWrapper *resource, PropertyKey id, const Value *receiver, bool
    *hasProperty, Value *base, Lookup *lookup)': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QV4.QQmlContextWrapper.getPropertyAndBase' has no cute function "
        "yet. Qt's 'ReturnedValue "
        "QV4::QQmlContextWrapper::getPropertyAndBase(const "
        "QQmlContextWrapper *resource, PropertyKey id, const Value "
        "*receiver, bool *hasProperty, Value *base, Lookup *lookup)': takes "
        "a number to change where it is.")
