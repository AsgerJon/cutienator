"""
QConnectedReplicaImplementation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QConnectedReplicaImplementation to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QRemoteObjectReplicaImplementation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QRemoteObjectReplica
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QRemoteObjectReplica = WAIT['QRemoteObjectReplica']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QConnectedReplicaImplementation(QRemoteObjectReplicaImplementation):
  """
  The cute side of Qt's QConnectedReplicaImplementation: a plain Python
  object standing in front of one C++ QConnectedReplicaImplementation.

  It is built on the cute 'QRemoteObjectReplicaImplementation', as Qt's
  QConnectedReplicaImplementation is built on Qt's
  QRemoteObjectReplicaImplementation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QConnectedReplicaImplementation that has a ritual
  and that Python can call so far, 8 names in all: 'getProperty',
  'setProperty', 'isShortCircuit', 'isInitialized', 'waitForSource',
  'configurePrivate', 'setDisconnected', 'setDynamicMetaObject'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QConnectedReplicaImplementation::setProperties(QVariantList
    &&a0)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<int> QConnectedReplicaImplementation::childIndices() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  12 of the 22 functions Qt declares: 10 leans on 'QRemoteObjectPackets; 2
  leans on 'QRemoteObjectPendingCallWatcherHelper.

  What to expect
  --------------

  - The C++ QConnectedReplicaImplementation is created at the first use, not
    by 'QConnectedReplicaImplementation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QConnectedReplicaImplementation.
  - Qt tells when it has removed the C++ QConnectedReplicaImplementation.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QConnectedReplicaImplementation that has no cute
    function yet, '__init__', 'childIndices', 'initialize',
    'requestRemoteObjectSource', 'sendCommand', 'sendCommandWithReply',
    'setConnection', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QConnectedReplicaImplementation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def getProperty(self, i: int) -> QVariant:
    """
    Calls Qt's 'const QVariant
    QConnectedReplicaImplementation::getProperty(int i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconnectedreplicaimplementation.html#getProperty

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  const QVariant QConnectedReplicaImplementation::getProperty(int i)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK31QConnectedReplicaImplementation11getPropertyEi', i,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isShortCircuit(self) -> bool:
    """
    Calls Qt's 'bool QConnectedReplicaImplementation::isShortCircuit()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconnectedreplicaimplementation.html
    """
    #  bool QConnectedReplicaImplementation::isShortCircuit() const
    return self.uglySide.call(
        'ritual_ZNK31QConnectedReplicaImplementation14isShortCircuitEv',
    )

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QConnectedReplicaImplementation::isInitialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconnectedreplicaimplementation.html#isInitialized
    """
    #  bool QConnectedReplicaImplementation::isInitialized() const
    return self.uglySide.call(
        'ritual_ZNK31QConnectedReplicaImplementation13isInitializedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QVariant)
  def setProperty(self, i: int, a1: QVariant) -> None:
    """
    Calls Qt's 'void QConnectedReplicaImplementation::setProperty(int i,
    const QVariant &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconnectedreplicaimplementation.html#setProperty

    Parameters
    ----------

    i : int
      Passed on as it is.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QConnectedReplicaImplementation::setProperty(int i, const
    #      QVariant &a1)
    self.uglySide.call(
        'ritual_ZN31QConnectedReplicaImplementation11setPropertyEiRK8QVaria'
        'nt',
        i, self._valueOf(a1),
    )

  def setDisconnected(self) -> None:
    """
    Calls Qt's 'void QConnectedReplicaImplementation::setDisconnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconnectedreplicaimplementation.html
    """
    #  void QConnectedReplicaImplementation::setDisconnected()
    self.uglySide.call(
        'ritual_ZN31QConnectedReplicaImplementation15setDisconnectedEv',
    )

  @overload(QMetaObject)
  @overload(NoneType)
  def setDynamicMetaObject(self, meta: Optional[QMetaObject]) -> None:
    """
    Calls Qt's 'void
    QConnectedReplicaImplementation::setDynamicMetaObject(const QMetaObject
    *meta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconnectedreplicaimplementation.html

    Parameters
    ----------

    meta : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QConnectedReplicaImplementation::setDynamicMetaObject(const
    #      QMetaObject *meta)
    self.uglySide.call(
        'ritual_ZN31QConnectedReplicaImplementation20setDynamicMetaObjectEP'
        'K11QMetaObject',
        self._addressOf(meta, 'QMetaObject'),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QConnectedReplicaImplementation::QConnectedReplicaImplementation(const
    QString &name, const QMetaObject *a1, QRemoteObjectNode *a2)': leans on
    'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QConnectedReplicaImplementation.__init__' has no cute function "
        "yet. Qt's "
        "'QConnectedReplicaImplementation::QConnectedReplicaImplementation(c"
        "onst QString &name, const QMetaObject *a1, QRemoteObjectNode "
        "*a2)': leans on "
        "'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @overload(int)
  def waitForSource(self, timeout: int) -> bool:
    """
    Calls Qt's 'bool QConnectedReplicaImplementation::waitForSource(int
    timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconnectedreplicaimplementation.html#waitForSource

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  bool QConnectedReplicaImplementation::waitForSource(int timeout)
    return self.uglySide.call(
        'ritual_ZN31QConnectedReplicaImplementation13waitForSourceEi',
        timeout,
    )

  @overload(QRemoteObjectReplica)
  @overload(NoneType)
  def configurePrivate(self, a0: Optional[QRemoteObjectReplica]) -> None:
    """
    Calls Qt's 'void
    QConnectedReplicaImplementation::configurePrivate(QRemoteObjectReplica
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qconnectedreplicaimplementation.html

    Parameters
    ----------

    a0 : Optional[QRemoteObjectReplica]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QConnectedReplicaImplementation::configurePrivate(
    #      QRemoteObjectReplica *a0)
    self.uglySide.call(
        'ritual_ZN31QConnectedReplicaImplementation16configurePrivateEP20QR'
        'emoteObjectReplica',
        self._addressOf(a0),
    )

  @staticmethod
  def childIndices(*__, **_) -> Never:
    """
    Qt's 'QList<int> QConnectedReplicaImplementation::childIndices() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QConnectedReplicaImplementation.childIndices' has no cute "
        "function yet. Qt's 'QList<int> "
        "QConnectedReplicaImplementation::childIndices() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'void QConnectedReplicaImplementation::initialize(QVariantList
    &&values)': leans on 'QRemoteObjectPackets::decodeVariant(QVariant&&,
    QMetaType)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QConnectedReplicaImplementation.initialize' has no cute function "
        "yet. Qt's 'void "
        "QConnectedReplicaImplementation::initialize(QVariantList "
        "&&values)': leans on "
        "'QRemoteObjectPackets::decodeVariant(QVariant&&, QMetaType)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def requestRemoteObjectSource(*__, **_) -> Never:
    """
    Qt's 'void QConnectedReplicaImplementation::requestRemoteObjectSource()':
    leans on 'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QConnectedReplicaImplementation.requestRemoteObjectSource' has no "
        "cute function yet. Qt's 'void "
        "QConnectedReplicaImplementation::requestRemoteObjectSource()': "
        "leans on "
        "'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def sendCommand(*__, **_) -> Never:
    """
    Qt's 'bool QConnectedReplicaImplementation::sendCommand()': leans on
    'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QConnectedReplicaImplementation.sendCommand' has no cute function "
        "yet. Qt's 'bool QConnectedReplicaImplementation::sendCommand()': "
        "leans on "
        "'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def sendCommandWithReply(*__, **_) -> Never:
    """
    Qt's 'QRemoteObjectPendingCall
    QConnectedReplicaImplementation::sendCommandWithReply(int serialId)':
    leans on 'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QConnectedReplicaImplementation.sendCommandWithReply' has no cute "
        "function yet. Qt's 'QRemoteObjectPendingCall "
        "QConnectedReplicaImplementation::sendCommandWithReply(int "
        "serialId)': leans on "
        "'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setConnection(*__, **_) -> Never:
    """
    Qt's 'void
    QConnectedReplicaImplementation::setConnection(QtROIoDeviceBase *conn)':
    leans on 'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QConnectedReplicaImplementation.setConnection' has no cute "
        "function yet. Qt's 'void "
        "QConnectedReplicaImplementation::setConnection(QtROIoDeviceBase "
        "*conn)': leans on "
        "'QRemoteObjectPackets::CodecBase::send(QtROIoDeviceBase*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
