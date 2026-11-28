"""
QDBusConnectionInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusconnectioninterface.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QDBusAbstractInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaMethod, QMetaObject
  from . import QDBusConnection, QDBusError, QDBusMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusConnection = WAIT['QDBusConnection']
  QDBusError = WAIT['QDBusError']
  QDBusMessage = WAIT['QDBusMessage']
  QMetaMethod = WAIT['QMetaMethod']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusConnectionInterface(QDBusAbstractInterface):
  """
  The cute side of Qt's QDBusConnectionInterface: a plain Python object
  standing in front of one C++ QDBusConnectionInterface.

  It is built on the cute 'QDBusAbstractInterface', as Qt's
  QDBusConnectionInterface is built on Qt's QDBusAbstractInterface, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusConnectionInterface that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr',
  'staticInterfaceName', 'serviceRegistered', 'serviceUnregistered',
  'serviceOwnerChanged', 'callWithCallbackFailed', 'NameAcquired',
  'NameLost', 'NameOwnerChanged', 'connectNotify', 'disconnectNotify'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusConnectionInterface::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QDBusConnectionInterface::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusConnectionInterface::~QDBusConnectionInterface()': the
    destructor: Python never removes a C++ QDBusConnectionInterface.
  - Qt's 'QDBusReply<QStringList>
    QDBusConnectionInterface::registeredServiceNames() const': gives a type
    Python has no way to take yet.
  - Qt's 'QDBusReply<QStringList>
    QDBusConnectionInterface::activatableServiceNames() const': gives a type
    Python has no way to take yet.
  - Qt's 'QDBusReply<bool>
    QDBusConnectionInterface::isServiceRegistered(const QString &serviceName)
    const': gives a type Python has no way to take yet.
  - Qt's 'QDBusReply<QString> QDBusConnectionInterface::serviceOwner(const
    QString &name) const': gives a type Python has no way to take yet.
  - Qt's 'QDBusReply<bool> QDBusConnectionInterface::unregisterService(const
    QString &serviceName)': gives a type Python has no way to take yet.
  - Qt's 'QDBusReply<QDBusConnectionInterface::RegisterServiceReply>
    QDBusConnectionInterface::registerService(const QString &serviceName,
    ServiceQueueOptions qoption, ServiceReplacementOptions roption)': gives a
    type Python has no way to take yet.
  - Qt's 'QDBusReply<uint> QDBusConnectionInterface::servicePid(const QString
    &serviceName) const': gives a type Python has no way to take yet.
  - Qt's 'QDBusReply<uint> QDBusConnectionInterface::serviceUid(const QString
    &serviceName) const': gives a type Python has no way to take yet.
  - Qt's 'QDBusReply<QVariantMap>
    QDBusConnectionInterface::serviceCredentials(const QString &serviceName)
    const': gives a type Python has no way to take yet.
  - Qt's 'QDBusReply<void> QDBusConnectionInterface::startService(const
    QString &name)': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDBusConnectionInterface is created at the first use, not by
    'QDBusConnectionInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusConnectionInterface.
  - Qt tells when it has removed the C++ QDBusConnectionInterface. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDBusConnectionInterface that has no cute function yet,
    'activatableServiceNames', 'isServiceRegistered', 'registerService',
    'registeredServiceNames', 'serviceCredentials', 'serviceOwner',
    'servicePid', 'serviceUid', 'startService', 'unregisterService', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDBusConnectionInterface, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class RegisterServiceReply(CuteNum):
    """
    The enum 'QDBusConnectionInterface::RegisterServiceReply' of Qt, with the
    3 names Qt gives in it.
    """

    ServiceNotRegistered = Kee[int](0)
    ServiceRegistered = Kee[int](1)
    ServiceQueued = Kee[int](2)

  class ServiceQueueOptions(CuteNum):
    """
    The enum 'QDBusConnectionInterface::ServiceQueueOptions' of Qt, with the
    3 names Qt gives in it.
    """

    DontQueueService = Kee[int](0)
    QueueService = Kee[int](1)
    ReplaceExistingService = Kee[int](2)

  class ServiceReplacementOptions(CuteNum):
    """
    The enum 'QDBusConnectionInterface::ServiceReplacementOptions' of Qt,
    with the 2 names Qt gives in it.
    """

    DontAllowReplacement = Kee[int](0)
    AllowReplacement = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QDBusConnectionInterface::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnectioninterface.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusConnectionInterface::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QDBusConnectionInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def staticInterfaceName() -> Optional[str]:
    """
    Calls Qt's 'const char *QDBusConnectionInterface::staticInterfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectioninterface.html#staticInterfaceName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QDBusConnectionInterface::staticInterfaceName()
    chars = Rituals.call(
        'ritual_ZN24QDBusConnectionInterface19staticInterfaceNameEv',
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusConnectionInterface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusConnectionInterface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectioninterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusConnectionInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QDBusConnectionInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QDBusConnection, QObject)
  @overload(QDBusConnection, NoneType)
  def __init__(
      self,
      connection: QDBusConnection,
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDBusConnectionInterface::QDBusConnectionInterface(const QDBusConnection
    &connection, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectioninterface.html

    Parameters
    ----------

    connection : QDBusConnection
      Passed on as a value: Qt reads the C++ QDBusConnection, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDBusConnectionInterface::QDBusConnectionInterface(const
    #      QDBusConnection &connection, QObject *parent)
    self._noteCreation(QDBusConnectionInterface, lambda: Rituals.call(
        'ritual_ZN24QDBusConnectionInterfaceC1ERK15QDBusConnectionP7QObject',
        self._valueOf(connection), self._addressOf(parent, 'QObject'),
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

  @overload(str)
  def serviceRegistered(self, service: str) -> None:
    """
    Calls Qt's 'void QDBusConnectionInterface::serviceRegistered(const
    QString &service)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectioninterface.html#serviceRegistered

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnectionInterface::serviceRegistered(const QString
    #      &service)
    self.uglySide.call(
        'ritual_ZN24QDBusConnectionInterface17serviceRegisteredERK7QString',
        service,
    )

  @overload(str)
  def serviceUnregistered(self, service: str) -> None:
    """
    Calls Qt's 'void QDBusConnectionInterface::serviceUnregistered(const
    QString &service)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectioninterface.html#serviceUnregistered

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnectionInterface::serviceUnregistered(const QString
    #      &service)
    self.uglySide.call(
        'ritual_ZN24QDBusConnectionInterface19serviceUnregisteredERK7QStrin'
        'g',
        service,
    )

  @overload(str, str, str)
  def serviceOwnerChanged(
      self,
      name: str,
      oldOwner: str,
      newOwner: str,
  ) -> None:
    """
    Calls Qt's 'void QDBusConnectionInterface::serviceOwnerChanged(const
    QString &name, const QString &oldOwner, const QString &newOwner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectioninterface.html#serviceOwnerChanged

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    oldOwner : str
      Passed on as it is: a QString is made of it for the call.

    newOwner : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnectionInterface::serviceOwnerChanged(const QString
    #      &name, const QString &oldOwner, const QString &newOwner)
    self.uglySide.call(
        'ritual_ZN24QDBusConnectionInterface19serviceOwnerChangedERK7QStrin'
        'gS2_S2_',
        name, oldOwner, newOwner,
    )

  @overload(QDBusError, QDBusMessage)
  def callWithCallbackFailed(
      self,
      error: QDBusError,
      call: QDBusMessage,
  ) -> None:
    """
    Calls Qt's 'void QDBusConnectionInterface::callWithCallbackFailed(const
    QDBusError &error, const QDBusMessage &call)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectioninterface.html

    Parameters
    ----------

    error : QDBusError
      Passed on as a value: Qt reads the C++ QDBusError, which stays Python's
      own.

    call : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  void QDBusConnectionInterface::callWithCallbackFailed(const QDBusError
    #      &error, const QDBusMessage &call)
    self.uglySide.call(
        'ritual_ZN24QDBusConnectionInterface22callWithCallbackFailedERK10QD'
        'BusErrorRK12QDBusMessage',
        self._valueOf(error), self._valueOf(call),
    )

  @overload(str)
  def NameAcquired(self, a0: str) -> None:
    """
    Calls Qt's 'void QDBusConnectionInterface::NameAcquired(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectioninterface.html#NameAcquired

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnectionInterface::NameAcquired(const QString &a0)
    self.uglySide.call(
        'ritual_ZN24QDBusConnectionInterface12NameAcquiredERK7QString', a0,
    )

  @overload(str)
  def NameLost(self, a0: str) -> None:
    """
    Calls Qt's 'void QDBusConnectionInterface::NameLost(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectioninterface.html#NameLost

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnectionInterface::NameLost(const QString &a0)
    self.uglySide.call(
        'ritual_ZN24QDBusConnectionInterface8NameLostERK7QString', a0,
    )

  @overload(str, str, str)
  def NameOwnerChanged(self, a0: str, a1: str, a2: str) -> None:
    """
    Calls Qt's 'void QDBusConnectionInterface::NameOwnerChanged(const QString
    &a0, const QString &a1, const QString &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectioninterface.html#NameOwnerChanged

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    a2 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnectionInterface::NameOwnerChanged(const QString &a0,
    #      const QString &a1, const QString &a2)
    self.uglySide.call(
        'ritual_ZN24QDBusConnectionInterface16NameOwnerChangedERK7QStringS2'
        '_S2_',
        a0, a1, a2,
    )

  @overload(QMetaMethod)
  def connectNotify(self, a0: QMetaMethod) -> None:
    """
    Calls Qt's 'void QDBusConnectionInterface::connectNotify(const
    QMetaMethod &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectioninterface.html#connectNotify

    Parameters
    ----------

    a0 : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QDBusConnectionInterface::connectNotify(const QMetaMethod &a0)
    ritual = (
        'ritual_ZN24QDBusConnectionInterface13connectNotifyERK11QMetaMethod')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QDBusConnectionInterface13connectNotifyERK11QMeta'
          'Method')
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QMetaMethod)
  def disconnectNotify(self, a0: QMetaMethod) -> None:
    """
    Calls Qt's 'void QDBusConnectionInterface::disconnectNotify(const
    QMetaMethod &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectioninterface.html#disconnectNotify

    Parameters
    ----------

    a0 : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QDBusConnectionInterface::disconnectNotify(const QMetaMethod &a0)
    ritual = (
        'ritual_ZN24QDBusConnectionInterface16disconnectNotifyERK11QMetaMet'
        'hod')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QDBusConnectionInterface16disconnectNotifyERK11QM'
          'etaMethod')
    self.uglySide.call(ritual, self._valueOf(a0))

  @staticmethod
  def activatableServiceNames(*__, **_) -> Never:
    """
    Qt's 'QDBusReply<QStringList>
    QDBusConnectionInterface::activatableServiceNames() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusConnectionInterface.activatableServiceNames' has no cute "
        "function yet. Qt's 'QDBusReply<QStringList> "
        "QDBusConnectionInterface::activatableServiceNames() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def isServiceRegistered(*__, **_) -> Never:
    """
    Qt's 'QDBusReply<bool>
    QDBusConnectionInterface::isServiceRegistered(const QString &serviceName)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusConnectionInterface.isServiceRegistered' has no cute "
        "function yet. Qt's 'QDBusReply<bool> "
        "QDBusConnectionInterface::isServiceRegistered(const QString "
        "&serviceName) const': gives a type Python has no way to take yet.")

  @staticmethod
  def registerService(*__, **_) -> Never:
    """
    Qt's 'QDBusReply<QDBusConnectionInterface::RegisterServiceReply>
    QDBusConnectionInterface::registerService(const QString &serviceName,
    ServiceQueueOptions qoption, ServiceReplacementOptions roption)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusConnectionInterface.registerService' has no cute function "
        "yet. Qt's "
        "'QDBusReply<QDBusConnectionInterface::RegisterServiceReply> "
        "QDBusConnectionInterface::registerService(const QString "
        "&serviceName, ServiceQueueOptions qoption, "
        "ServiceReplacementOptions roption)': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def registeredServiceNames(*__, **_) -> Never:
    """
    Qt's 'QDBusReply<QStringList>
    QDBusConnectionInterface::registeredServiceNames() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusConnectionInterface.registeredServiceNames' has no cute "
        "function yet. Qt's 'QDBusReply<QStringList> "
        "QDBusConnectionInterface::registeredServiceNames() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def serviceCredentials(*__, **_) -> Never:
    """
    Qt's 'QDBusReply<QVariantMap>
    QDBusConnectionInterface::serviceCredentials(const QString &serviceName)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusConnectionInterface.serviceCredentials' has no cute function "
        "yet. Qt's 'QDBusReply<QVariantMap> "
        "QDBusConnectionInterface::serviceCredentials(const QString "
        "&serviceName) const': gives a type Python has no way to take yet.")

  @staticmethod
  def serviceOwner(*__, **_) -> Never:
    """
    Qt's 'QDBusReply<QString> QDBusConnectionInterface::serviceOwner(const
    QString &name) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusConnectionInterface.serviceOwner' has no cute function yet. "
        "Qt's 'QDBusReply<QString> "
        "QDBusConnectionInterface::serviceOwner(const QString &name) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def servicePid(*__, **_) -> Never:
    """
    Qt's 'QDBusReply<uint> QDBusConnectionInterface::servicePid(const QString
    &serviceName) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusConnectionInterface.servicePid' has no cute function yet. "
        "Qt's 'QDBusReply<uint> QDBusConnectionInterface::servicePid(const "
        "QString &serviceName) const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def serviceUid(*__, **_) -> Never:
    """
    Qt's 'QDBusReply<uint> QDBusConnectionInterface::serviceUid(const QString
    &serviceName) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusConnectionInterface.serviceUid' has no cute function yet. "
        "Qt's 'QDBusReply<uint> QDBusConnectionInterface::serviceUid(const "
        "QString &serviceName) const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def startService(*__, **_) -> Never:
    """
    Qt's 'QDBusReply<void> QDBusConnectionInterface::startService(const
    QString &name)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusConnectionInterface.startService' has no cute function yet. "
        "Qt's 'QDBusReply<void> "
        "QDBusConnectionInterface::startService(const QString &name)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def unregisterService(*__, **_) -> Never:
    """
    Qt's 'QDBusReply<bool> QDBusConnectionInterface::unregisterService(const
    QString &serviceName)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusConnectionInterface.unregisterService' has no cute function "
        "yet. Qt's 'QDBusReply<bool> "
        "QDBusConnectionInterface::unregisterService(const QString "
        "&serviceName)': gives a type Python has no way to take yet.")
