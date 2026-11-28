"""
QV4::QmlListWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmllistwrapper_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::QmlListWrapper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaType, QObject, QVariant
  from . import QQmlListReference, QQmlProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QObject = WAIT['QObject']
  QQmlProperty = WAIT['QQmlProperty']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlListWrapper(QV4.Object):
  """
  The cute side of Qt's QV4::QmlListWrapper: a plain Python object standing
  in front of one C++ QV4::QmlListWrapper.

  It is built on the cute 'QV4::Object', as Qt's QV4::QmlListWrapper is built
  on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::QmlListWrapper that has a ritual and that
  Python can call so far, 11 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualDestroy', 'defaultPrototype', 'create', 'createOwned', 'toVariant',
  'toListReference', 'virtualGetLength', 'virtualPut'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::QmlListWrapper::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'ReturnedValue QV4::QmlListWrapper::create(ExecutionEngine *engine,
    const QQmlListProperty<QObject> &prop, QMetaType propType)': takes a type
    Python has no way to hand over yet.
  - Qt's 'ReturnedValue QV4::QmlListWrapper::virtualGet(const Managed *m,
    PropertyKey id, const Value *receiver, bool *hasProperty)': takes a
    number to change where it is.
  - Qt's 'OwnPropertyKeyIterator
    *QV4::QmlListWrapper::virtualOwnPropertyKeys(const Object *m, Value
    *target)': gives 'QV4::OwnPropertyKeyIterator', which has no cute class
    yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::QmlListWrapper is created at the first use, not by
    'QV4::QmlListWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::QmlListWrapper.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::QmlListWrapper::virtualDestroy(QV4::Heap::Base
    *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmllistwrapper.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::QmlListWrapper::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV414QmlListWrapper14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::QmlListWrapper::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmllistwrapper.html#defaultPrototype

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
    #      *QV4::QmlListWrapper::defaultPrototype(QV4::ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV414QmlListWrapper16defaultPrototypeEPNS_15ExecutionEng'
        'ineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QObject, int, QMetaType)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, int, QMetaType)
  @overload(NoneType, QObject, int, QMetaType)
  @overload(NoneType, NoneType, int, QMetaType)
  def create(
      engine: Optional[QV4.ExecutionEngine],
      object: Optional[QObject],
      propId: int,
      propType: QMetaType,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QmlListWrapper::create(ExecutionEngine
    *engine, QObject *object, int propId, QMetaType propType)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmllistwrapper.html#create

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propId : int
      Passed on as it is.

    propType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  ReturnedValue QV4::QmlListWrapper::create(ExecutionEngine *engine,
    #      QObject *object, int propId, QMetaType propType)
    return Rituals.call(
        'ritual_ZN3QV414QmlListWrapper6createEPNS_15ExecutionEngineEP7QObje'
        'cti9QMetaType',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(object,
        'QObject'), propId, CuteMixin._valueOf(propType),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QMetaType)
  @overload(NoneType, QMetaType)
  def create(
      engine: Optional[QV4.ExecutionEngine],
      propType: QMetaType,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::QmlListWrapper::create(ExecutionEngine
    *engine, QMetaType propType)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmllistwrapper.html#create

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  ReturnedValue QV4::QmlListWrapper::create(ExecutionEngine *engine,
    #      QMetaType propType)
    return Rituals.call(
        'ritual_ZN3QV414QmlListWrapper6createEPNS_15ExecutionEngineE9QMetaT'
        'ype',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(propType),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QQmlProperty)
  @overload(NoneType, QQmlProperty)
  def createOwned(
      engine: Optional[QV4.ExecutionEngine],
      prop: QQmlProperty,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::QmlListWrapper::createOwned(ExecutionEngine *engine, const
    QQmlProperty &prop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmllistwrapper.html#createOwned

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    prop : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  ReturnedValue QV4::QmlListWrapper::createOwned(ExecutionEngine
    #      *engine, const QQmlProperty &prop)
    return Rituals.call(
        'ritual_ZN3QV414QmlListWrapper11createOwnedEPNS_15ExecutionEngineER'
        'K12QQmlProperty',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(prop),
    )

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualGetLength(m: Optional[QV4.Managed]) -> int:
    """
    Calls Qt's 'qint64 QV4::QmlListWrapper::virtualGetLength(const Managed
    *m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmllistwrapper.html#virtualGetLength

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qint64 QV4::QmlListWrapper::virtualGetLength(const Managed *m)
    return Rituals.call(
        'ritual_ZN3QV414QmlListWrapper16virtualGetLengthEPKNS_7ManagedE',
        CuteMixin._addressOf(m),
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
    Calls Qt's 'bool QV4::QmlListWrapper::virtualPut(Managed *m, PropertyKey
    id, const Value &value, Value *receiver)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmllistwrapper.html#virtualPut

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
    #  bool QV4::QmlListWrapper::virtualPut(Managed *m, PropertyKey id, const
    #      Value &value, Value *receiver)
    return Rituals.call(
        'ritual_ZN3QV414QmlListWrapper10virtualPutEPNS_7ManagedENS_11Proper'
        'tyKeyERKNS_5ValueEPS4_',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._valueOf(value), CuteMixin._addressOf(receiver),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::QmlListWrapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.QmlListWrapper]:
    """
    Calls Qt's 'QV4::Heap::QmlListWrapper *QV4::QmlListWrapper::d_unchecked()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmllistwrapper.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.QmlListWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QmlListWrapper *QV4::QmlListWrapper::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV414QmlListWrapper11d_uncheckedEv',
    )
    return QV4.Heap.QmlListWrapper._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.QmlListWrapper]:
    """
    Calls Qt's 'QV4::Heap::QmlListWrapper *QV4::QmlListWrapper::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmllistwrapper.html#d

    Returns
    -------

    Optional[QV4.Heap.QmlListWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::QmlListWrapper *QV4::QmlListWrapper::d() const
    address = self.uglySide.call('ritual_ZNK3QV414QmlListWrapper1dEv')
    return QV4.Heap.QmlListWrapper._cuteAt(address)

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QV4::QmlListWrapper::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmllistwrapper.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QV4::QmlListWrapper::toVariant() const
    address = self.uglySide.call(
        'ritual_ZNK3QV414QmlListWrapper9toVariantEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def toListReference(self) -> QQmlListReference:
    """
    Calls Qt's 'QQmlListReference QV4::QmlListWrapper::toListReference()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-qmllistwrapper.html#toListReference

    Returns
    -------

    QQmlListReference
      A new cute QQmlListReference around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlListReference QV4::QmlListWrapper::toListReference() const
    address = self.uglySide.call(
        'ritual_ZNK3QV414QmlListWrapper15toListReferenceEv',
    )
    from . import QQmlListReference
    return QQmlListReference._cuteOwning(address)

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
    Calls Qt's 'void QV4::QmlListWrapper::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-qmllistwrapper.html#__dataTest
    """
    #  void QV4::QmlListWrapper::__dataTest()
    self.uglySide.call('ritual_ZN3QV414QmlListWrapper10__dataTestEv')
