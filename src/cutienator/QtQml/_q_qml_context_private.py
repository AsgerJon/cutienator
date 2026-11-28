"""
QQmlContextPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlcontext_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlContextPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QVariant
  from . import QQmlContext, QQmlContextData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlContext = WAIT['QQmlContext']
  QQmlContextData = WAIT['QQmlContextData']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlContextPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQmlContextPrivate: a plain Python object standing in
  front of one C++ QQmlContextPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQmlContextPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlContextPrivate that has a ritual and that Python
  can call so far, 11 names in all: 'q_func', 'get', 'notifyIndex',
  'setNotifyIndex', 'numPropertyValues', 'appendPropertyValue',
  'setPropertyValue', 'propertyValue', 'appendInstance', 'cleanInstances',
  'emitDestruction'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlContext *QQmlContextPrivate::q_func() const': takes in
    Python what 'QQmlContext *QQmlContextPrivate::q_func()' takes.
  - Qt's 'qsizetype
    QQmlContextPrivate::context_count(QQmlListProperty<QObject> *a0)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QQmlContextPrivate::context_at(QQmlListProperty<QObject>
    *a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'QList<QPointer<QObject>> QQmlContextPrivate::instances() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlContextPrivate::QQmlContextPrivate(QQmlContext *publicContext,
    const QQmlRefPointer<QQmlContextData> &parent, QQmlEngine *engine)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 19 functions Qt declares: 1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QQmlContextPrivate is created at the first use, not by
    'QQmlContextPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlContextPrivate.
  - Each name of Qt's QQmlContextPrivate that has no cute function yet,
    'context_at', 'context_count', 'dropDestroyedQObject', 'instances', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlContext)
  @overload(NoneType)
  def get(context: Optional[QQmlContext]) -> Optional[QQmlContextPrivate]:
    """
    Calls Qt's 'QQmlContextPrivate *QQmlContextPrivate::get(QQmlContext
    *context)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextprivate.html#get

    Parameters
    ----------

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlContextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContextPrivate *QQmlContextPrivate::get(QQmlContext *context)
    address = Rituals.call(
        'ritual_ZN18QQmlContextPrivate3getEP11QQmlContext',
        CuteMixin._addressOf(context),
    )
    return QQmlContextPrivate._cuteAt(address)

  @staticmethod
  @overload(THIS)
  def get(context: Optional[QQmlContextPrivate]) -> Optional[QQmlContext]:
    """
    Calls Qt's 'QQmlContext *QQmlContextPrivate::get(QQmlContextPrivate
    *context)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextprivate.html#get

    Parameters
    ----------

    context : Optional[QQmlContextPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContext *QQmlContextPrivate::get(QQmlContextPrivate *context)
    address = Rituals.call(
        'ritual_ZN18QQmlContextPrivate3getEPS_',
        CuteMixin._addressOf(context),
    )
    from . import QQmlContext
    return QQmlContext._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlContextPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def notifyIndex(self) -> int:
    """
    Calls Qt's 'int QQmlContextPrivate::notifyIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextprivate.html#notifyIndex
    """
    #  int QQmlContextPrivate::notifyIndex() const
    return self.uglySide.call(
        'ritual_ZNK18QQmlContextPrivate11notifyIndexEv',
    )

  def numPropertyValues(self) -> int:
    """
    Calls Qt's 'int QQmlContextPrivate::numPropertyValues() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextprivate.html#numPropertyValues
    """
    #  int QQmlContextPrivate::numPropertyValues() const
    return self.uglySide.call(
        'ritual_ZNK18QQmlContextPrivate17numPropertyValuesEv',
    )

  @overload(int)
  def propertyValue(self, index: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlContextPrivate::propertyValue(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextprivate.html#propertyValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlContextPrivate::propertyValue(int index) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlContextPrivate13propertyValueEi', index,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setNotifyIndex(self, notifyIndex: int) -> None:
    """
    Calls Qt's 'void QQmlContextPrivate::setNotifyIndex(int notifyIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextprivate.html#setNotifyIndex

    Parameters
    ----------

    notifyIndex : int
      Passed on as it is.
    """
    #  void QQmlContextPrivate::setNotifyIndex(int notifyIndex)
    self.uglySide.call(
        'ritual_ZN18QQmlContextPrivate14setNotifyIndexEi', notifyIndex,
    )

  @overload(int, QVariant)
  def setPropertyValue(self, index: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlContextPrivate::setPropertyValue(int index, const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextprivate.html#setPropertyValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlContextPrivate::setPropertyValue(int index, const QVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN18QQmlContextPrivate16setPropertyValueEiRK8QVariant',
        index, self._valueOf(value),
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

  @overload(QQmlContextData)
  @overload(NoneType)
  def __init__(self, data: Optional[QQmlContextData]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlContextPrivate::QQmlContextPrivate(QQmlContextData *data)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextprivate.html#QQmlContextPrivate

    Parameters
    ----------

    data : Optional[QQmlContextData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlContextPrivate::QQmlContextPrivate(QQmlContextData *data)
    self._noteCreation(QQmlContextPrivate, lambda: Rituals.call(
        'ritual_ZN18QQmlContextPrivateC1EP15QQmlContextData',
        self._addressOf(data),
    ))

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

  def q_func(self) -> Optional[QQmlContext]:
    """
    Calls Qt's 'QQmlContext *QQmlContextPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextprivate.html#q_func

    Returns
    -------

    Optional[QQmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContext *QQmlContextPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QQmlContextPrivate6q_funcEv')
    from . import QQmlContext
    return QQmlContext._cuteAt(address)

  @overload(QVariant)
  def appendPropertyValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlContextPrivate::appendPropertyValue(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextprivate.html#appendPropertyValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlContextPrivate::appendPropertyValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN18QQmlContextPrivate19appendPropertyValueERK8QVariant',
        self._valueOf(value),
    )

  @overload(QObject)
  @overload(NoneType)
  def appendInstance(self, instance: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlContextPrivate::appendInstance(QObject *instance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextprivate.html#appendInstance

    Parameters
    ----------

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContextPrivate::appendInstance(QObject *instance)
    self.uglySide.call(
        'ritual_ZN18QQmlContextPrivate14appendInstanceEP7QObject',
        self._addressOf(instance, 'QObject'),
    )

  def cleanInstances(self) -> None:
    """
    Calls Qt's 'void QQmlContextPrivate::cleanInstances()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextprivate.html#cleanInstances
    """
    #  void QQmlContextPrivate::cleanInstances()
    self.uglySide.call('ritual_ZN18QQmlContextPrivate14cleanInstancesEv')

  def emitDestruction(self) -> None:
    """
    Calls Qt's 'void QQmlContextPrivate::emitDestruction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextprivate.html#emitDestruction
    """
    #  void QQmlContextPrivate::emitDestruction()
    self.uglySide.call('ritual_ZN18QQmlContextPrivate15emitDestructionEv')

  @staticmethod
  def context_at(*__, **_) -> Never:
    """
    Qt's 'QObject *QQmlContextPrivate::context_at(QQmlListProperty<QObject>
    *a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQmlContextPrivate.context_at' has no cute function yet. Qt's "
        "'QObject *QQmlContextPrivate::context_at(QQmlListProperty<QObject> "
        "*a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has "
        "no cute class yet.")

  @staticmethod
  def context_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQmlContextPrivate::context_count(QQmlListProperty<QObject> *a0)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlContextPrivate.context_count' has no cute function yet. Qt's "
        "'qsizetype "
        "QQmlContextPrivate::context_count(QQmlListProperty<QObject> *a0)': "
        "names 'QQmlListProperty<QObject>', which has no cute class yet.")

  @staticmethod
  def dropDestroyedQObject(*__, **_) -> Never:
    """
    Qt's 'void QQmlContextPrivate::dropDestroyedQObject(const QString &name,
    QObject *destroyed)': leans on 'QV4::IdentifierHash::toIdentifier(QString
    const&) const', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlContextPrivate.dropDestroyedQObject' has no cute function "
        "yet. Qt's 'void QQmlContextPrivate::dropDestroyedQObject(const "
        "QString &name, QObject *destroyed)': leans on "
        "'QV4::IdentifierHash::toIdentifier(QString const&) const', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def instances(*__, **_) -> Never:
    """
    Qt's 'QList<QPointer<QObject>> QQmlContextPrivate::instances() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlContextPrivate.instances' has no cute function yet. Qt's "
        "'QList<QPointer<QObject>> QQmlContextPrivate::instances() const': "
        "gives a type Python has no way to take yet.")
