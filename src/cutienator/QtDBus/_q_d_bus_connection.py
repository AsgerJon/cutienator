"""
QDBusConnection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusconnection.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QDBus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QObject
  from . import QDBusConnectionInterface, QDBusConnectionPrivate, QDBusError
  from . import QDBusMessage, QDBusPendingCall, QDBusVirtualObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusConnectionPrivate = WAIT['QDBusConnectionPrivate']
  QDBusMessage = WAIT['QDBusMessage']
  QDBusVirtualObject = WAIT['QDBusVirtualObject']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusConnection(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusConnection: a plain Python object standing in
  front of one C++ QDBusConnection.

  C++ hands a QDBusConnection around as a copy, so every C++ QDBusConnection
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusConnection that has a ritual and that Python
  can call so far, 25 names in all: 'isConnected', 'baseService',
  'lastError', 'name', 'connectionCapabilities', 'send', 'callWithCallback',
  'call', 'asyncCall', 'connect', 'disconnect', 'registerObject',
  'unregisterObject', 'objectRegisteredAt', 'registerVirtualObject',
  'registerService', 'unregisterService', 'interface', 'connectToBus',
  'connectToPeer', 'disconnectFromBus', 'disconnectFromPeer',
  'localMachineId', 'sessionBus', 'systemBus'. It can be made from Python, in
  3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusConnection::QDBusConnection(QDBusConnection &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QDBusConnection &QDBusConnection::operator=(QDBusConnection
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QDBusConnection &QDBusConnection::operator=(const QDBusConnection
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QDBusConnection::~QDBusConnection()': the destructor: Python
    removes its C++ QDBusConnection by it, and has no other use for it.
  - Qt's 'void QDBusConnection::swap(QDBusConnection &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void *QDBusConnection::internalPointer() const': gives 'void',
    which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 44 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QDBusConnection is created at the first use, not by
    'QDBusConnection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusConnection back gives a copy the ritual made for
    Python, in a new cute QDBusConnection.
  - Each name of Qt's QDBusConnection that has no cute function yet,
    'internalPointer', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDBusConnection, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class BusType(CuteNum):
    """
    The enum 'QDBusConnection::BusType' of Qt, with the 3 names Qt gives in
    it.
    """

    SessionBus = Kee[int](0)
    SystemBus = Kee[int](1)
    ActivationBus = Kee[int](2)

  class ConnectionCapability(CuteFlags):
    """
    The flags enum 'QDBusConnection::ConnectionCapability' of Qt, with the 1
    names Qt gives in it. Qt names the type of its combinations
    'QDBusConnection::ConnectionCapabilities'.
    """

    UnixFileDescriptorPassing = 0x1

  ConnectionCapabilities = ConnectionCapability

  class RegisterOption(CuteFlags):
    """
    The flags enum 'QDBusConnection::RegisterOption' of Qt, with the 18 names
    Qt gives in it. Qt names the type of its combinations
    'QDBusConnection::RegisterOptions'.
    """

    ExportAdaptors = 0x1
    ExportScriptableSlots = 0x10
    ExportScriptableSignals = 0x20
    ExportScriptableProperties = 0x40
    ExportScriptableInvokables = 0x80
    ExportScriptableContents = 0xf0
    ExportNonScriptableSlots = 0x100
    ExportNonScriptableSignals = 0x200
    ExportNonScriptableProperties = 0x400
    ExportNonScriptableInvokables = 0x800
    ExportNonScriptableContents = 0xf00
    ExportAllSlots = 0x110
    ExportAllSignals = 0x220
    ExportAllProperties = 0x440
    ExportAllInvokables = 0x880
    ExportAllContents = 0xff0
    ExportAllSignal = 0x220
    ExportChildObjects = 0x1000

  RegisterOptions = RegisterOption

  class UnregisterMode(CuteNum):
    """
    The enum 'QDBusConnection::UnregisterMode' of Qt, with the 2 names Qt
    gives in it.
    """

    UnregisterNode = Kee[int](0)
    UnregisterTree = Kee[int](1)

  class VirtualObjectRegisterOption(CuteFlags):
    """
    The flags enum 'QDBusConnection::VirtualObjectRegisterOption' of Qt, with
    the 2 names Qt gives in it. Qt names the type of its combinations
    'QDBusConnection::VirtualObjectRegisterOptions'.
    """

    SingleNode = 0x0
    SubPath = 0x1

  VirtualObjectRegisterOptions = VirtualObjectRegisterOption

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(BusType, str)
  def connectToBus(type: BusType, name: str) -> QDBusConnection:
    """
    Calls Qt's 'QDBusConnection QDBusConnection::connectToBus(BusType type,
    const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#connectToBus

    Parameters
    ----------

    type : BusType
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusConnection
      A new cute QDBusConnection around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusConnection QDBusConnection::connectToBus(BusType type, const
    #      QString &name)
    address = Rituals.call(
        'ritual_ZN15QDBusConnection12connectToBusENS_7BusTypeERK7QString',
        type.value, name,
    )
    return QDBusConnection._cuteOwning(address)

  @staticmethod
  @overload(str, str)
  def connectToBus(address: str, name: str) -> QDBusConnection:
    """
    Calls Qt's 'QDBusConnection QDBusConnection::connectToBus(const QString
    &address, const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#connectToBus

    Parameters
    ----------

    address : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusConnection
      A new cute QDBusConnection around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusConnection QDBusConnection::connectToBus(const QString &address,
    #      const QString &name)
    address = Rituals.call(
        'ritual_ZN15QDBusConnection12connectToBusERK7QStringS2_',
        address, name,
    )
    return QDBusConnection._cuteOwning(address)

  @staticmethod
  @overload(str, str)
  def connectToPeer(address: str, name: str) -> QDBusConnection:
    """
    Calls Qt's 'QDBusConnection QDBusConnection::connectToPeer(const QString
    &address, const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#connectToPeer

    Parameters
    ----------

    address : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusConnection
      A new cute QDBusConnection around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusConnection QDBusConnection::connectToPeer(const QString &address,
    #      const QString &name)
    address = Rituals.call(
        'ritual_ZN15QDBusConnection13connectToPeerERK7QStringS2_',
        address, name,
    )
    return QDBusConnection._cuteOwning(address)

  @staticmethod
  @overload(str)
  def disconnectFromBus(name: str) -> None:
    """
    Calls Qt's 'void QDBusConnection::disconnectFromBus(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#disconnectFromBus

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnection::disconnectFromBus(const QString &name)
    Rituals.call(
        'ritual_ZN15QDBusConnection17disconnectFromBusERK7QString', name,
    )

  @staticmethod
  @overload(str)
  def disconnectFromPeer(name: str) -> None:
    """
    Calls Qt's 'void QDBusConnection::disconnectFromPeer(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#disconnectFromPeer

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnection::disconnectFromPeer(const QString &name)
    Rituals.call(
        'ritual_ZN15QDBusConnection18disconnectFromPeerERK7QString', name,
    )

  @staticmethod
  def localMachineId() -> QByteArray:
    """
    Calls Qt's 'QByteArray QDBusConnection::localMachineId()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#localMachineId

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QDBusConnection::localMachineId()
    address = Rituals.call('ritual_ZN15QDBusConnection14localMachineIdEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def sessionBus() -> QDBusConnection:
    """
    Calls Qt's 'QDBusConnection QDBusConnection::sessionBus()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#sessionBus

    Returns
    -------

    QDBusConnection
      A new cute QDBusConnection around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusConnection QDBusConnection::sessionBus()
    address = Rituals.call('ritual_ZN15QDBusConnection10sessionBusEv')
    return QDBusConnection._cuteOwning(address)

  @staticmethod
  def systemBus() -> QDBusConnection:
    """
    Calls Qt's 'QDBusConnection QDBusConnection::systemBus()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#systemBus

    Returns
    -------

    QDBusConnection
      A new cute QDBusConnection around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusConnection QDBusConnection::systemBus()
    address = Rituals.call('ritual_ZN15QDBusConnection9systemBusEv')
    return QDBusConnection._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusConnection'

  #  Qt's '~QDBusConnection()'. Naming it makes this a value class: Python
  #  owns every C++ QDBusConnection behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QDBusConnectionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isConnected(self) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::isConnected() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#isConnected
    """
    #  bool QDBusConnection::isConnected() const
    return self.uglySide.call('ritual_ZNK15QDBusConnection11isConnectedEv')

  def baseService(self) -> str:
    """
    Calls Qt's 'QString QDBusConnection::baseService() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#baseService

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusConnection::baseService() const
    return self.uglySide.call('ritual_ZNK15QDBusConnection11baseServiceEv')

  def lastError(self) -> QDBusError:
    """
    Calls Qt's 'QDBusError QDBusConnection::lastError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#lastError

    Returns
    -------

    QDBusError
      A new cute QDBusError around the copy Qt gave back. Python owns it.
    """
    #  QDBusError QDBusConnection::lastError() const
    address = self.uglySide.call('ritual_ZNK15QDBusConnection9lastErrorEv')
    from . import QDBusError
    return QDBusError._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QDBusConnection::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusConnection::name() const
    return self.uglySide.call('ritual_ZNK15QDBusConnection4nameEv')

  def connectionCapabilities(self) -> ConnectionCapabilities:
    """
    Calls Qt's 'ConnectionCapabilities
    QDBusConnection::connectionCapabilities() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#connectionCapabilities

    Returns
    -------

    ConnectionCapabilities
      The value standing for the combination Qt gave back.
    """
    #  ConnectionCapabilities QDBusConnection::connectionCapabilities() const
    return QDBusConnection.ConnectionCapabilities(self.uglySide.call(
        'ritual_ZNK15QDBusConnection22connectionCapabilitiesEv',
    ))

  @overload(QDBusMessage)
  def send(self, message: QDBusMessage) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::send(const QDBusMessage &message)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#send

    Parameters
    ----------

    message : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  bool QDBusConnection::send(const QDBusMessage &message) const
    return self.uglySide.call(
        'ritual_ZNK15QDBusConnection4sendERK12QDBusMessage',
        self._valueOf(message),
    )

  @overload(QDBusMessage, QObject, str, str)
  @overload(QDBusMessage, QObject, str, NoneType)
  @overload(QDBusMessage, QObject, NoneType, str)
  @overload(QDBusMessage, QObject, NoneType, NoneType)
  @overload(QDBusMessage, NoneType, str, str)
  @overload(QDBusMessage, NoneType, str, NoneType)
  @overload(QDBusMessage, NoneType, NoneType, str)
  @overload(QDBusMessage, NoneType, NoneType, NoneType)
  @overload(QDBusMessage, QObject, str, str, int)
  @overload(QDBusMessage, QObject, str, NoneType, int)
  @overload(QDBusMessage, QObject, NoneType, str, int)
  @overload(QDBusMessage, QObject, NoneType, NoneType, int)
  @overload(QDBusMessage, NoneType, str, str, int)
  @overload(QDBusMessage, NoneType, str, NoneType, int)
  @overload(QDBusMessage, NoneType, NoneType, str, int)
  @overload(QDBusMessage, NoneType, NoneType, NoneType, int)
  def callWithCallback(
      self,
      message: QDBusMessage,
      receiver: Optional[QObject],
      returnMethod: Optional[str],
      errorMethod: Optional[str],
      timeout: int = -1,
  ) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::callWithCallback(const QDBusMessage
    &message, QObject *receiver, const char *returnMethod, const char
    *errorMethod, int timeout) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#callWithCallback

    Parameters
    ----------

    message : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    returnMethod : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    errorMethod : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  bool QDBusConnection::callWithCallback(const QDBusMessage &message,
    #      QObject *receiver, const char *returnMethod, const char
    #      *errorMethod, int timeout) const
    return self.uglySide.call(
        'ritual_ZNK15QDBusConnection16callWithCallbackERK12QDBusMessageP7QO'
        'bjectPKcS6_i',
        self._valueOf(message), self._addressOf(receiver, 'QObject'),
        self._bytesOf(returnMethod), self._bytesOf(errorMethod), timeout,
    )

  @overload(QDBusMessage, QObject, str)
  @overload(QDBusMessage, QObject, NoneType)
  @overload(QDBusMessage, NoneType, str)
  @overload(QDBusMessage, NoneType, NoneType)
  @overload(QDBusMessage, QObject, str, int)
  @overload(QDBusMessage, QObject, NoneType, int)
  @overload(QDBusMessage, NoneType, str, int)
  @overload(QDBusMessage, NoneType, NoneType, int)
  def callWithCallback(
      self,
      message: QDBusMessage,
      receiver: Optional[QObject],
      slot: Optional[str],
      timeout: int = -1,
  ) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::callWithCallback(const QDBusMessage
    &message, QObject *receiver, const char *slot, int timeout) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#callWithCallback

    Parameters
    ----------

    message : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    slot : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  bool QDBusConnection::callWithCallback(const QDBusMessage &message,
    #      QObject *receiver, const char *slot, int timeout) const
    return self.uglySide.call(
        'ritual_ZNK15QDBusConnection16callWithCallbackERK12QDBusMessageP7QO'
        'bjectPKci',
        self._valueOf(message), self._addressOf(receiver, 'QObject'),
        self._bytesOf(slot), timeout,
    )

  @overload(QDBusMessage)
  @overload(QDBusMessage, QDBus.CallMode)
  @overload(QDBusMessage, QDBus.CallMode, int)
  def call(
      self,
      message: QDBusMessage,
      mode: QDBus.CallMode = QDBus.CallMode.Block,
      timeout: int = -1,
  ) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusConnection::call(const QDBusMessage
    &message, QDBus::CallMode mode, int timeout) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#call

    Parameters
    ----------

    message : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.

    mode : QDBus.CallMode
      Passed on as its number. May be left out, as in Qt: it is then
      QDBus.CallMode.Block.

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusConnection::call(const QDBusMessage &message,
    #      QDBus::CallMode mode, int timeout) const
    address = self.uglySide.call(
        'ritual_ZNK15QDBusConnection4callERK12QDBusMessageN5QDBus8CallModeE'
        'i',
        self._valueOf(message), mode.value, timeout,
    )
    from . import QDBusMessage
    return QDBusMessage._cuteOwning(address)

  @overload(QDBusMessage)
  @overload(QDBusMessage, int)
  def asyncCall(
      self,
      message: QDBusMessage,
      timeout: int = -1,
  ) -> QDBusPendingCall:
    """
    Calls Qt's 'QDBusPendingCall QDBusConnection::asyncCall(const
    QDBusMessage &message, int timeout) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#asyncCall

    Parameters
    ----------

    message : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.

    timeout : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QDBusPendingCall
      A new cute QDBusPendingCall around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusPendingCall QDBusConnection::asyncCall(const QDBusMessage
    #      &message, int timeout) const
    address = self.uglySide.call(
        'ritual_ZNK15QDBusConnection9asyncCallERK12QDBusMessagei',
        self._valueOf(message), timeout,
    )
    from . import QDBusPendingCall
    return QDBusPendingCall._cuteOwning(address)

  @overload(str)
  def objectRegisteredAt(self, path: str) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QDBusConnection::objectRegisteredAt(const QString
    &path) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#objectRegisteredAt

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QDBusConnection::objectRegisteredAt(const QString &path)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QDBusConnection18objectRegisteredAtERK7QString', path,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def interface(self) -> Optional[QDBusConnectionInterface]:
    """
    Calls Qt's 'QDBusConnectionInterface *QDBusConnection::interface()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#interface

    Returns
    -------

    Optional[QDBusConnectionInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusConnectionInterface *QDBusConnection::interface() const
    address = self.uglySide.call('ritual_ZNK15QDBusConnection9interfaceEv')
    from . import QDBusConnectionInterface
    return QDBusConnectionInterface._cuteAt(address)

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

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's 'QDBusConnection::QDBusConnection(const
    QString &name)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#QDBusConnection

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QDBusConnection::QDBusConnection(const QString &name)
    self._noteCreation(QDBusConnection, lambda: Rituals.call(
        'ritual_ZN15QDBusConnectionC1ERK7QString', name,
    ))

  @overload(THIS)
  def __init__(self, other: QDBusConnection) -> None:
    """
    Notes what was given, for Qt's 'QDBusConnection::QDBusConnection(const
    QDBusConnection &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#QDBusConnection

    Parameters
    ----------

    other : QDBusConnection
      Passed on as a value: Qt reads the C++ QDBusConnection, which stays
      Python's own.
    """
    #  QDBusConnection::QDBusConnection(const QDBusConnection &other)
    self._noteCreation(QDBusConnection, lambda: Rituals.call(
        'ritual_ZN15QDBusConnectionC1ERKS_', self._valueOf(other),
    ))

  @overload(QDBusConnectionPrivate)
  @overload(NoneType)
  def __init__(self, dd: Optional[QDBusConnectionPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDBusConnection::QDBusConnection(QDBusConnectionPrivate *dd)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#QDBusConnection

    Parameters
    ----------

    dd : Optional[QDBusConnectionPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDBusConnection::QDBusConnection(QDBusConnectionPrivate *dd)
    self._noteCreation(QDBusConnection, lambda: Rituals.call(
        'ritual_ZN15QDBusConnectionC1EP22QDBusConnectionPrivate',
        self._addressOf(dd),
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

  @overload(str, str, str, str, QObject, str)
  @overload(str, str, str, str, QObject, NoneType)
  @overload(str, str, str, str, NoneType, str)
  @overload(str, str, str, str, NoneType, NoneType)
  def connect(
      self,
      service: str,
      path: str,
      interface: str,
      name: str,
      receiver: Optional[QObject],
      slot: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::connect(const QString &service, const
    QString &path, const QString &interface, const QString &name, QObject
    *receiver, const char *slot)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#connect

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.

    path : str
      Passed on as it is: a QString is made of it for the call.

    interface : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    slot : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QDBusConnection::connect(const QString &service, const QString
    #      &path, const QString &interface, const QString &name, QObject
    #      *receiver, const char *slot)
    return self.uglySide.call(
        'ritual_ZN15QDBusConnection7connectERK7QStringS2_S2_S2_P7QObjectPKc',
        service, path, interface, name, self._addressOf(receiver, 'QObject'),
        self._bytesOf(slot),
    )

  @overload(str, str, str, str, str, QObject, str)
  @overload(str, str, str, str, str, QObject, NoneType)
  @overload(str, str, str, str, str, NoneType, str)
  @overload(str, str, str, str, str, NoneType, NoneType)
  def connect(
      self,
      service: str,
      path: str,
      interface: str,
      name: str,
      signature: str,
      receiver: Optional[QObject],
      slot: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::connect(const QString &service, const
    QString &path, const QString &interface, const QString &name, const
    QString &signature, QObject *receiver, const char *slot)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#connect

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.

    path : str
      Passed on as it is: a QString is made of it for the call.

    interface : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    signature : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    slot : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QDBusConnection::connect(const QString &service, const QString
    #      &path, const QString &interface, const QString &name, const
    #      QString &signature, QObject *receiver, const char *slot)
    return self.uglySide.call(
        'ritual_ZN15QDBusConnection7connectERK7QStringS2_S2_S2_S2_P7QObject'
        'PKc',
        service, path, interface, name, signature, self._addressOf(receiver,
        'QObject'), self._bytesOf(slot),
    )

  @overload(str, str, str, str, QStringList, str, QObject, str)
  @overload(str, str, str, str, QStringList, str, QObject, NoneType)
  @overload(str, str, str, str, QStringList, str, NoneType, str)
  @overload(str, str, str, str, QStringList, str, NoneType, NoneType)
  def connect(
      self,
      service: str,
      path: str,
      interface: str,
      name: str,
      argumentMatch: QStringList,
      signature: str,
      receiver: Optional[QObject],
      slot: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::connect(const QString &service, const
    QString &path, const QString &interface, const QString &name, const
    QStringList &argumentMatch, const QString &signature, QObject *receiver,
    const char *slot)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#connect

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.

    path : str
      Passed on as it is: a QString is made of it for the call.

    interface : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    argumentMatch : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    signature : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    slot : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QDBusConnection::connect(const QString &service, const QString
    #      &path, const QString &interface, const QString &name, const
    #      QStringList &argumentMatch, const QString &signature, QObject
    #      *receiver, const char *slot)
    return self.uglySide.call(
        'ritual_ZN15QDBusConnection7connectERK7QStringS2_S2_S2_RK5QListIS0_'
        'ES2_P7QObjectPKc',
        service, path, interface, name, self._valueOf(argumentMatch),
        signature, self._addressOf(receiver, 'QObject'), self._bytesOf(slot),
    )

  @overload(str, str, str, str, QObject, str)
  @overload(str, str, str, str, QObject, NoneType)
  @overload(str, str, str, str, NoneType, str)
  @overload(str, str, str, str, NoneType, NoneType)
  def disconnect(
      self,
      service: str,
      path: str,
      interface: str,
      name: str,
      receiver: Optional[QObject],
      slot: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::disconnect(const QString &service,
    const QString &path, const QString &interface, const QString &name,
    QObject *receiver, const char *slot)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#disconnect

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.

    path : str
      Passed on as it is: a QString is made of it for the call.

    interface : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    slot : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QDBusConnection::disconnect(const QString &service, const QString
    #      &path, const QString &interface, const QString &name, QObject
    #      *receiver, const char *slot)
    return self.uglySide.call(
        'ritual_ZN15QDBusConnection10disconnectERK7QStringS2_S2_S2_P7QObjec'
        'tPKc',
        service, path, interface, name, self._addressOf(receiver, 'QObject'),
        self._bytesOf(slot),
    )

  @overload(str, str, str, str, str, QObject, str)
  @overload(str, str, str, str, str, QObject, NoneType)
  @overload(str, str, str, str, str, NoneType, str)
  @overload(str, str, str, str, str, NoneType, NoneType)
  def disconnect(
      self,
      service: str,
      path: str,
      interface: str,
      name: str,
      signature: str,
      receiver: Optional[QObject],
      slot: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::disconnect(const QString &service,
    const QString &path, const QString &interface, const QString &name, const
    QString &signature, QObject *receiver, const char *slot)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#disconnect

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.

    path : str
      Passed on as it is: a QString is made of it for the call.

    interface : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    signature : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    slot : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QDBusConnection::disconnect(const QString &service, const QString
    #      &path, const QString &interface, const QString &name, const
    #      QString &signature, QObject *receiver, const char *slot)
    return self.uglySide.call(
        'ritual_ZN15QDBusConnection10disconnectERK7QStringS2_S2_S2_S2_P7QOb'
        'jectPKc',
        service, path, interface, name, signature, self._addressOf(receiver,
        'QObject'), self._bytesOf(slot),
    )

  @overload(str, str, str, str, QStringList, str, QObject, str)
  @overload(str, str, str, str, QStringList, str, QObject, NoneType)
  @overload(str, str, str, str, QStringList, str, NoneType, str)
  @overload(str, str, str, str, QStringList, str, NoneType, NoneType)
  def disconnect(
      self,
      service: str,
      path: str,
      interface: str,
      name: str,
      argumentMatch: QStringList,
      signature: str,
      receiver: Optional[QObject],
      slot: Optional[str],
  ) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::disconnect(const QString &service,
    const QString &path, const QString &interface, const QString &name, const
    QStringList &argumentMatch, const QString &signature, QObject *receiver,
    const char *slot)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnection.html#disconnect

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.

    path : str
      Passed on as it is: a QString is made of it for the call.

    interface : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    argumentMatch : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    signature : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    slot : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QDBusConnection::disconnect(const QString &service, const QString
    #      &path, const QString &interface, const QString &name, const
    #      QStringList &argumentMatch, const QString &signature, QObject
    #      *receiver, const char *slot)
    return self.uglySide.call(
        'ritual_ZN15QDBusConnection10disconnectERK7QStringS2_S2_S2_RK5QList'
        'IS0_ES2_P7QObjectPKc',
        service, path, interface, name, self._valueOf(argumentMatch),
        signature, self._addressOf(receiver, 'QObject'), self._bytesOf(slot),
    )

  @overload(str, QObject)
  @overload(str, NoneType)
  @overload(str, QObject, RegisterOptions)
  @overload(str, NoneType, RegisterOptions)
  def registerObject(
      self,
      path: str,
      object: Optional[QObject],
      options: RegisterOptions = RegisterOptions.ExportAdaptors,
  ) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::registerObject(const QString &path,
    QObject *object, RegisterOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#registerObject

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    options : RegisterOptions
      Passed on as its number. May be left out, as in Qt: it is then
      RegisterOptions.ExportAdaptors.
    """
    #  bool QDBusConnection::registerObject(const QString &path, QObject
    #      *object, RegisterOptions options)
    return self.uglySide.call(
        'ritual_ZN15QDBusConnection14registerObjectERK7QStringP7QObject6QFl'
        'agsINS_14RegisterOptionEE',
        path, self._addressOf(object, 'QObject'), options.value,
    )

  @overload(str, str, QObject)
  @overload(str, str, NoneType)
  @overload(str, str, QObject, RegisterOptions)
  @overload(str, str, NoneType, RegisterOptions)
  def registerObject(
      self,
      path: str,
      interface: str,
      object: Optional[QObject],
      options: RegisterOptions = RegisterOptions.ExportAdaptors,
  ) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::registerObject(const QString &path,
    const QString &interface, QObject *object, RegisterOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#registerObject

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    interface : str
      Passed on as it is: a QString is made of it for the call.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    options : RegisterOptions
      Passed on as its number. May be left out, as in Qt: it is then
      RegisterOptions.ExportAdaptors.
    """
    #  bool QDBusConnection::registerObject(const QString &path, const
    #      QString &interface, QObject *object, RegisterOptions options)
    return self.uglySide.call(
        'ritual_ZN15QDBusConnection14registerObjectERK7QStringS2_P7QObject6'
        'QFlagsINS_14RegisterOptionEE',
        path, interface, self._addressOf(object, 'QObject'), options.value,
    )

  @overload(str)
  @overload(str, UnregisterMode)
  def unregisterObject(
      self,
      path: str,
      mode: UnregisterMode = UnregisterMode.UnregisterNode,
  ) -> None:
    """
    Calls Qt's 'void QDBusConnection::unregisterObject(const QString &path,
    UnregisterMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#unregisterObject

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    mode : UnregisterMode
      Passed on as its number. May be left out, as in Qt: it is then
      UnregisterMode.UnregisterNode.
    """
    #  void QDBusConnection::unregisterObject(const QString &path,
    #      UnregisterMode mode)
    self.uglySide.call(
        'ritual_ZN15QDBusConnection16unregisterObjectERK7QStringNS_14Unregi'
        'sterModeE',
        path, mode.value,
    )

  @overload(str, QDBusVirtualObject)
  @overload(str, NoneType)
  @overload(str, QDBusVirtualObject, VirtualObjectRegisterOption)
  @overload(str, NoneType, VirtualObjectRegisterOption)
  def registerVirtualObject(
      self,
      path: str,
      object: Optional[QDBusVirtualObject],
      options: VirtualObjectRegisterOption = (
          VirtualObjectRegisterOption.SingleNode),
  ) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::registerVirtualObject(const QString
    &path, QDBusVirtualObject *object, VirtualObjectRegisterOption options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#registerVirtualObject

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    object : Optional[QDBusVirtualObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    options : VirtualObjectRegisterOption
      Passed on as its number. May be left out, as in Qt: it is then
      VirtualObjectRegisterOption.SingleNode.
    """
    #  bool QDBusConnection::registerVirtualObject(const QString &path,
    #      QDBusVirtualObject *object, VirtualObjectRegisterOption options)
    return self.uglySide.call(
        'ritual_ZN15QDBusConnection21registerVirtualObjectERK7QStringP18QDB'
        'usVirtualObjectNS_27VirtualObjectRegisterOptionE',
        path, self._addressOf(object), options.value,
    )

  @overload(str)
  def registerService(self, serviceName: str) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::registerService(const QString
    &serviceName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#registerService

    Parameters
    ----------

    serviceName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDBusConnection::registerService(const QString &serviceName)
    return self.uglySide.call(
        'ritual_ZN15QDBusConnection15registerServiceERK7QString',
        serviceName,
    )

  @overload(str)
  def unregisterService(self, serviceName: str) -> bool:
    """
    Calls Qt's 'bool QDBusConnection::unregisterService(const QString
    &serviceName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnection.html#unregisterService

    Parameters
    ----------

    serviceName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDBusConnection::unregisterService(const QString &serviceName)
    return self.uglySide.call(
        'ritual_ZN15QDBusConnection17unregisterServiceERK7QString',
        serviceName,
    )

  @staticmethod
  def internalPointer(*__, **_) -> Never:
    """
    Qt's 'void *QDBusConnection::internalPointer() const': gives 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDBusConnection.internalPointer' has no cute function yet. Qt's "
        "'void *QDBusConnection::internalPointer() const': gives 'void', "
        "which has no cute class yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnection::swap(QDBusConnection &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusConnection.swap' has no cute function yet. Qt's 'void "
        "QDBusConnection::swap(QDBusConnection &other)': takes a type "
        "Python has no way to hand over yet.")
